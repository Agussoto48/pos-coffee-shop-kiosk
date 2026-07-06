from __future__ import annotations
from pos_coffee_shop_kiosk.domain.factories.abstract_payment_factory import AbstractPaymentFactory
from pos_coffee_shop_kiosk.application.dtos.client_payment_details import ClientPaymentDetails
from pos_coffee_shop_kiosk.infrastructure.payment_methods.tap_card_payment_method import TapCardPaymentMethod


class TapCardPaymentFactory(AbstractPaymentFactory):

    def create(self, clientDetails: ClientPaymentDetails) -> TapCardPaymentMethod:
        if clientDetails.card_number is None:
            raise ValueError("El número de tarjeta es requerido")

        if clientDetails.card_holder is None:
            raise ValueError("El titular de la tarjeta es requerido")

        return TapCardPaymentMethod(
            card_number=clientDetails.card_number,
            card_holder=clientDetails.card_holder,
        )