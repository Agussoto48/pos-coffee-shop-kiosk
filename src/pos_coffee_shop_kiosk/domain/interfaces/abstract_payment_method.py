from __future__ import annotations
from abc import ABC, abstractmethod
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.models.entities.sale import Sale


class AbstractPaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount_due: Money) -> Sale:
        pass