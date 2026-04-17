from __future__ import annotations
from abc import ABC, abstractmethod
from pos_coffee_shop_kiosk.application.dtos.client_payment_details import ClientPaymentDetails
from pos_coffee_shop_kiosk.domain.interfaces.abstract_payment_method import AbstractPaymentMethod


class AbstractPaymentFactory(ABC):

    @abstractmethod
    def create(
        self,
        clientDetails: ClientPaymentDetails
    ) -> AbstractPaymentMethod:
        pass