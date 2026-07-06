from __future__ import annotations
from datetime import datetime
from pos_coffee_shop_kiosk.domain.interfaces.abstract_payment_method import AbstractPaymentMethod
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money


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

    def pay(self, amount_due: Money) -> None:
        if not self._card_number or len(self._card_number) < 4:
            raise ValueError("Número de tarjeta inválido")

        if not self._card_holder:
            raise ValueError("El titular de la tarjeta es requerido")

        if self._expiration_date < datetime.now():
            raise ValueError("La tarjeta está vencida")

        if not self._security_code:
            raise ValueError("El código de seguridad es requerido")

        print("Pago con tarjeta aprobado.")