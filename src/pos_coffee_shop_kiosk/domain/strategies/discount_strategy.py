from __future__ import annotations
from abc import ABC, abstractmethod

from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: Money) -> Money:
        pass