from __future__ import annotations

from typing import Mapping

from pos_coffee_shop_kiosk.application.dtos.checkout_result import (
    CheckoutPreview,
    CheckoutResult,
)
from pos_coffee_shop_kiosk.application.use_cases.shopping_cart.add_cart_item import AddCartItem
from pos_coffee_shop_kiosk.application.use_cases.shopping_cart.clear_cart import ClearCart
from pos_coffee_shop_kiosk.application.use_cases.shopping_cart.remove_cart_item import RemoveCartItem
from pos_coffee_shop_kiosk.domain.interfaces.abstract_payment_gateway import AbstractPaymentGateway
from pos_coffee_shop_kiosk.domain.interfaces.abstract_receipt_service import (
    AbstractReceiptService,
    ReceiptLine,
    ReceiptRequest,
)
from pos_coffee_shop_kiosk.domain.models.shopping_cart import ShoppingCart
from pos_coffee_shop_kiosk.domain.pricing.pricing_component import PricingComponent


class POSFacade:
    """Interfaz simple para el flujo de carrito, cálculo, pago y comprobante.

    La fachada coordina objetos especializados sin absorber su lógica. El
    cliente de presentación solo conoce este objeto y no necesita comunicarse
    directamente con repositorios, decoradores, pasarelas ni Hacienda.
    """

    def __init__(
        self,
        add_cart_item: AddCartItem,
        remove_cart_item: RemoveCartItem,
        clear_cart: ClearCart,
        shopping_cart: ShoppingCart,
        payment_gateway: AbstractPaymentGateway,
        receipt_service: AbstractReceiptService,
    ) -> None:
        self._add_cart_item = add_cart_item
        self._remove_cart_item = remove_cart_item
        self._clear_cart = clear_cart
        self._shopping_cart = shopping_cart
        self._payment_gateway = payment_gateway
        self._receipt_service = receipt_service

    def add_product(self, product_sku: str, quantity: int) -> None:
        self._add_cart_item.execute(product_sku, quantity)

    def remove_product(self, product_sku: str, quantity: int) -> None:
        self._remove_cart_item.execute(product_sku, quantity)

    def clear(self) -> None:
        self._clear_cart.execute()

    def preview(self, pricing: PricingComponent) -> CheckoutPreview:
        if self._shopping_cart.is_empty():
            raise ValueError("No se puede calcular una venta con el carrito vacío")
        return CheckoutPreview(
            total=pricing.calculate_total(),
            breakdown=tuple(pricing.breakdown()),
        )

    def checkout(
        self,
        pricing: PricingComponent,
        payment_data: Mapping[str, str],
        customer_identification: str | None = None,
    ) -> CheckoutResult:
        preview = self.preview(pricing)
        payment = self._payment_gateway.charge(preview.total, payment_data)

        if not payment.approved or payment.transaction_id is None:
            return CheckoutResult(
                completed=False,
                total=preview.total,
                transaction_id=payment.transaction_id,
                message=payment.message,
                receipt=None,
            )

        receipt_request = ReceiptRequest(
            transaction_id=payment.transaction_id,
            total=preview.total,
            lines=tuple(
                ReceiptLine(
                    description=str(item.product().name()),
                    quantity=item.quantity(),
                    unit_price=item.product().price(),
                )
                for item in self._shopping_cart.items()
            ),
            customer_identification=customer_identification,
        )
        receipt = self._receipt_service.issue(receipt_request)

        if not receipt.accepted:
            return CheckoutResult(
                completed=False,
                total=preview.total,
                transaction_id=payment.transaction_id,
                message=f"Pago aprobado, pero el comprobante fue rechazado: {receipt.message}",
                receipt=receipt,
            )

        self._clear_cart.execute()
        return CheckoutResult(
            completed=True,
            total=preview.total,
            transaction_id=payment.transaction_id,
            message="Venta completada correctamente",
            receipt=receipt,
        )
