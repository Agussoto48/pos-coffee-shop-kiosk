from __future__ import annotations
from abc import ABC, abstractmethod
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money


class AbstractPaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount_due: Money) -> None:
        pass