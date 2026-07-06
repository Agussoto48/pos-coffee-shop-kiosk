"""Demostración autocontenida de los patrones asignados a la Persona B."""

from decimal import Decimal

from pos_coffee_shop_kiosk.application.facades.pos_facade import POSFacade
from pos_coffee_shop_kiosk.application.use_cases.shopping_cart.add_cart_item import AddCartItem
from pos_coffee_shop_kiosk.application.use_cases.shopping_cart.clear_cart import ClearCart
from pos_coffee_shop_kiosk.application.use_cases.shopping_cart.remove_cart_item import RemoveCartItem
from pos_coffee_shop_kiosk.domain.models.shopping_cart import ShoppingCart
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.pricing.price_decorators import (
    PercentageDiscountDecorator,
    TaxDecorator,
    ThresholdPromotionDecorator,
)
from pos_coffee_shop_kiosk.domain.pricing.pricing_component import CartSubtotal
from pos_coffee_shop_kiosk.infrastructure.adapters.hacienda_receipt_adapter import (
    HaciendaReceiptAdapter,
)
from pos_coffee_shop_kiosk.infrastructure.payment_gateways.simulated_payment_gateway import (
    SimulatedPaymentGateway,
)
from pos_coffee_shop_kiosk.infrastructure.repositories.json_product_repository import (
    JsonProductRepository,
)


class SimulatedHaciendaApi:
    def send_xml(self, api_token: str, xml_document: str) -> dict[str, object]:
        if not api_token or "<Comprobante>" not in xml_document:
            return {"estado": "rechazado", "mensaje": "Documento inválido"}
        return {
            "estado": "aceptado",
            "clave": "506-DEMO-0001",
            "mensaje": "Comprobante aceptado",
        }


def main() -> None:
    repository = JsonProductRepository("san_jose_db.json")
    cart = ShoppingCart()
    facade = POSFacade(
        add_cart_item=AddCartItem(repository, cart),
        remove_cart_item=RemoveCartItem(repository, cart),
        clear_cart=ClearCart(cart),
        shopping_cart=cart,
        payment_gateway=SimulatedPaymentGateway(),
        receipt_service=HaciendaReceiptAdapter(SimulatedHaciendaApi(), "token-demo"),
    )

    facade.add_product("19", 2)

    pricing = CartSubtotal(cart)
    pricing = PercentageDiscountDecorator(pricing, Decimal("5"), "Descuento estudiante")
    pricing = ThresholdPromotionDecorator(
        pricing,
        minimum_purchase=Money(Decimal("3000"), cart.items()[0].product().price().currency()),
        discount=Money(Decimal("250"), cart.items()[0].product().price().currency()),
        description="Promoción de cafetería",
    )
    pricing = TaxDecorator(pricing, Decimal("13"), "Impuesto de venta")

    preview = facade.preview(pricing)
    print("\nDETALLE DEL CÁLCULO")
    for line in preview.breakdown:
        sign = "-" if line.kind == "discount" else "+"
        print(f"{sign} {line.description}: {line.amount}")
    print(f"TOTAL: {preview.total}")

    result = facade.checkout(pricing, {"method": "card"}, "CONSUMIDOR_FINAL")
    print("\nRESULTADO DEL CHECKOUT")
    print(result.message)
    print(f"Transacción: {result.transaction_id}")
    if result.receipt:
        print(f"Comprobante: {result.receipt.receipt_key}")


if __name__ == "__main__":
    main()
