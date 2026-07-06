from __future__ import annotations
from pos_coffee_shop_kiosk.domain.factories.abstract_payment_factory import AbstractPaymentFactory
from pos_coffee_shop_kiosk.application.dtos.client_payment_details import ClientPaymentDetails
from pos_coffee_shop_kiosk.infrastructure.payment_methods.card_payment_method import CardPaymentMethod


class CardPaymentFactory(AbstractPaymentFactory):

    def create(self, clientDetails: ClientPaymentDetails) -> CardPaymentMethod:
        if clientDetails.card_number is None:
            raise ValueError("El número de tarjeta es requerido")

        if clientDetails.card_holder is None:
            raise ValueError("El titular de la tarjeta es requerido")

        if clientDetails.expiration_date is None:
            raise ValueError("La fecha de expiración es requerida")

        if clientDetails.security_code is None:
            raise ValueError("El código de seguridad es requerido")

        return CardPaymentMethod(
            card_number=clientDetails.card_number,
            card_holder=clientDetails.card_holder,
            expiration_date=clientDetails.expiration_date,
            security_code=str(clientDetails.security_code),
        )