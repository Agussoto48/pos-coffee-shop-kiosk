from __future__ import annotations
from pos_coffee_shop_kiosk.domain.interfaces.abstract_payment_method import AbstractPaymentMethod
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.models.entities.sale import Sale


class TapCardPaymentMethod(AbstractPaymentMethod):

    def __init__(self, card_number: str, card_holder: str) -> None:
        self._card_number = card_number
        self._card_holder = card_holder

    def pay(self, amount_due: Money) -> Sale:
        pass