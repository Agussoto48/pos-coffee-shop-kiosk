from __future__ import annotations
from uuid import UUID
from datetime import datetime

from pos_coffee_shop_kiosk.domain.factories.abstract_sale_factory import AbstractSaleFactory
from pos_coffee_shop_kiosk.domain.models.entities.electronic_sale import ElectronicSale
from pos_coffee_shop_kiosk.domain.models.shopping_cart import ShoppingCart
from pos_coffee_shop_kiosk.domain.enums.payment_method_type import PaymentMethodType
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.enums.sale_status import SaleStatus


class ElectronicSaleFactory(AbstractSaleFactory):
    def create(
        self,
        sale_id: UUID,
        cart: ShoppingCart,
        payment_method: PaymentMethodType,
        amount_paid: Money,
        change: Money | None = None,
        status: SaleStatus = SaleStatus.PENDING,
        timestamp: datetime | None = None,
    ) -> ElectronicSale:
        return ElectronicSale(
            sale_id=sale_id,
            cart=cart,
            payment_method=payment_method,
            amount_paid=amount_paid,
            change=change,
            status=status,
            timestamp=timestamp,
        )