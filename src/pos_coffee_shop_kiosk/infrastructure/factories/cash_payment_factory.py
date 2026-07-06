from __future__ import annotations
from pos_coffee_shop_kiosk.domain.enums.currency import Currency
from pos_coffee_shop_kiosk.domain.factories.abstract_payment_factory import AbstractPaymentFactory
from pos_coffee_shop_kiosk.application.dtos.client_payment_details import ClientPaymentDetails
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.infrastructure.payment_methods.cash_payment_method import CashPaymentMethod


class CashPaymentFactory(AbstractPaymentFactory):

    def create(self, clientDetails: ClientPaymentDetails) -> CashPaymentMethod:
        if clientDetails.amount_tendered is None:
            raise ValueError("El monto entregado es requerido para pago en efectivo")

        return CashPaymentMethod(
            Money(clientDetails.amount_tendered, Currency.COLONES)
        )