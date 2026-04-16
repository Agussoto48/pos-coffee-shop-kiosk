from __future__ import annotations
from uuid import UUID
from datetime import datetime

from pos_coffee_shop_kiosk.domain.models.shopping_cart import ShoppingCart
from pos_coffee_shop_kiosk.domain.enums.payment_method_type import PaymentMethodType
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.enums.sale_status import SaleStatus


class Sale:
    _sale_id: UUID
    _cart: ShoppingCart
    _payment_method: PaymentMethodType
    _amount_paid: Money
    _change: Money | None
    _status: SaleStatus
    _timestamp: datetime

    def __init__(
        self,
        sale_id: UUID,
        cart: ShoppingCart,
        payment_method: PaymentMethodType,
        amount_paid: Money,
        change: Money | None = None,
        status: SaleStatus = SaleStatus.PENDING,
        timestamp: datetime = datetime.now(),
    ) -> None:
        self._sale_id = sale_id
        self._cart = cart
        self._payment_method = payment_method
        self._amount_paid = amount_paid
        self._change = change
        self._status = status
        self._timestamp = timestamp

    def complete(self) -> None:
        pass

    def fail(self) -> None:
        pass

    def sale_id(self) -> UUID:
        pass

    def cart(self) -> ShoppingCart:
        pass

    def payment_method(self) -> PaymentMethodType:
        pass

    def amount_paid(self) -> Money:
        pass

    def change(self) -> Money | None:
        pass

    def status(self) -> SaleStatus:
        pass

    def timestamp(self) -> datetime:
        pass