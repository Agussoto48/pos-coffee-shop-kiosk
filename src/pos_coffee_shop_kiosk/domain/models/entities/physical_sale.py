from uuid import UUID
from datetime import datetime

from pos_coffee_shop_kiosk.domain.models.entities.sale import Sale
from pos_coffee_shop_kiosk.domain.models.shopping_cart import ShoppingCart
from pos_coffee_shop_kiosk.domain.enums.payment_method_type import PaymentMethodType
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.enums.sale_status import SaleStatus

class PhysicalSale(Sale):

    def __init__(
        self,
        sale_id: UUID,
        cart: ShoppingCart,
        payment_method: PaymentMethodType,
        amount_paid: Money,
        change: Money | None = None,
        status: SaleStatus = SaleStatus.PENDING,
        timestamp: datetime | None = None,
    ) -> None:
        super().__init__(
            sale_id,
            cart,
            payment_method,
            amount_paid,
            change,
            status,
            timestamp or datetime.now()
        )

    def complete(self) -> None:
        print(f"[PhysicalSale] Generando ticket fisico para venta {self._sale_id}...")
        print("[PhysicalSale] Enviando comando de impresion a la impresora...")
        super().complete()
        print(f"[PhysicalSale] Venta {self._sale_id} completada")

    def fail(self) -> None:
        print(f"[PhysicalSale] Error al imprimir el ticket fisico de la venta {self._sale_id}.")
        super().fail()
        print(f"[PhysicalSale] Venta {self._sale_id} marcada como fallida")