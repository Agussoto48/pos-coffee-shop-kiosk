from __future__ import annotations
from pos_coffee_shop_kiosk.domain.interfaces.abstract_payment_method import AbstractPaymentMethod
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money


class CashPaymentMethod(AbstractPaymentMethod):

    def __init__(self, amount_tendered: Money) -> None:
        self._amount_tendered = amount_tendered

    def pay(self, amount_due: Money) -> None:
        if self._amount_tendered.currency() != amount_due.currency():
            raise ValueError("La moneda del pago no coincide con la moneda del total")

        if self._amount_tendered.amount() < amount_due.amount():
            raise ValueError("El monto entregado es insuficiente")

        print("Pago en efectivo aprobado.")