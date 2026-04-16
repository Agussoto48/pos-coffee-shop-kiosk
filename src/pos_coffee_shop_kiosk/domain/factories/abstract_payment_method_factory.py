from __future__ import annotations
from abc import ABC, abstractmethod
from pos_coffee_shop_kiosk.domain.enums.payment_method_type import PaymentMethodType
from pos_coffee_shop_kiosk.domain.models.dtos.client_payment_details import ClientPaymentDetails
from pos_coffee_shop_kiosk.domain.interfaces.abstract_payment_method import AbstractPaymentMethod


class AbstractPaymentMethodFactory(ABC):

    @abstractmethod
    def create(
        self,
        methodType: PaymentMethodType,
        clientDetails: ClientPaymentDetails
    ) -> AbstractPaymentMethod:
        pass