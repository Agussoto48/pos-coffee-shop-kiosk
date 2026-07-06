from __future__ import annotations
from pos_coffee_shop_kiosk.application.dtos.client_payment_details import ClientPaymentDetails
from pos_coffee_shop_kiosk.domain.enums.payment_method_type import PaymentMethodType
from pos_coffee_shop_kiosk.domain.factories.abstract_payment_method_factory import AbstractPaymentMethodFactory
from pos_coffee_shop_kiosk.domain.interfaces.abstract_payment_method import AbstractPaymentMethod


class CreatePaymentMethod:
    def __init__(
        self,
        paymentMethodFactory: AbstractPaymentMethodFactory,
    ) -> None:
        self.paymentMethodFactory = paymentMethodFactory

    def execute(
        self,
        methodType: PaymentMethodType,
        clientDetails: ClientPaymentDetails,
    ) -> AbstractPaymentMethod:
        return self.paymentMethodFactory.create(methodType, clientDetails)