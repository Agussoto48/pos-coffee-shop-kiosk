from __future__ import annotations
from datetime import datetime
from pos_coffee_shop_kiosk.domain.interfaces.abstract_payment_method import AbstractPaymentMethod
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.models.entities.sale import Sale


class CardPaymentMethod(AbstractPaymentMethod):

    def __init__(
        self,
        card_number: str,
        card_holder: str,
        expiration_date: datetime,
        security_code: str,
    ) -> None:
        self._card_number = card_number
        self._card_holder = card_holder
        self._expiration_date = expiration_date
        self._security_code = security_code

    def pay(self, amount_due: Money) -> Sale:
        pass