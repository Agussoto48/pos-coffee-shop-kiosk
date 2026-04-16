from __future__ import annotations
from pos_coffee_shop_kiosk.domain.factories.abstract_payment_factory import AbstractPaymentFactory
from pos_coffee_shop_kiosk.domain.models.dtos.client_payment_details import ClientPaymentDetails
from pos_coffee_shop_kiosk.infrastructure.payment_methods.cash_payment_method import CashPaymentMethod


class CashPaymentFactory(AbstractPaymentFactory):

    def create(self, clientDetails: ClientPaymentDetails) -> CashPaymentMethod:
        pass