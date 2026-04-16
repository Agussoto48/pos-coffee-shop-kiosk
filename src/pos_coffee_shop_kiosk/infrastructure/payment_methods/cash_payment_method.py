from __future__ import annotations
from pos_coffee_shop_kiosk.domain.interfaces.abstract_payment_method import AbstractPaymentMethod
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.models.entities.sale import Sale


class CashPaymentMethod(AbstractPaymentMethod):

    def __init__(self, amount_tendered: Money) -> None:
        self._amount_tendered = amount_tendered

    def pay(self, amount_due: Money) -> Sale:
        pass