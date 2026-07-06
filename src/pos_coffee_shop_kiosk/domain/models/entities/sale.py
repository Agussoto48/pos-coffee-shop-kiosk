from __future__ import annotations
from uuid import UUID
from datetime import datetime
from pos_coffee_shop_kiosk.domain.models.shopping_cart import ShoppingCart
from pos_coffee_shop_kiosk.domain.enums.payment_method_type import PaymentMethodType
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.enums.sale_status import SaleStatus
from pos_coffee_shop_kiosk.domain.states.pending_sale_state import PendingSaleState
from pos_coffee_shop_kiosk.domain.states.success_sale_state import SuccessSaleState
from pos_coffee_shop_kiosk.domain.states.failure_sale_state import FailureSaleState


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
        timestamp: datetime | None = None,
    ) -> None:
        self._sale_id = sale_id
        self._cart = cart
        self._payment_method = payment_method
        self._amount_paid = amount_paid
        self._change = change
        self._status = status
        self._timestamp = timestamp or datetime.now()

        self._pending_state = PendingSaleState()
        self._success_state = SuccessSaleState()
        self._failure_state = FailureSaleState()

        if status == SaleStatus.PENDING:
            self._state = self._pending_state
        elif status == SaleStatus.SUCCESS:
            self._state = self._success_state
        elif status == SaleStatus.FAILURE:
            self._state = self._failure_state
        else:
            raise ValueError("Estado de venta inválido")

    def complete(self) -> None:
        self._state.complete(self)

    def fail(self) -> None:
        self._state.fail(self)

    def sale_id(self) -> UUID:
        return self._sale_id

    def cart(self) -> ShoppingCart:
        return self._cart

    def payment_method(self) -> PaymentMethodType:
        return self._payment_method

    def amount_paid(self) -> Money:
        return self._amount_paid

    def change(self) -> Money | None:
        return self._change

    def status(self) -> SaleStatus:
        return self._status

    def timestamp(self) -> datetime:
        return self._timestamp