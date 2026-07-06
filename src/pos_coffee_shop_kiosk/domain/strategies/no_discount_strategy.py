from __future__ import annotations

from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.strategies.discount_strategy import DiscountStrategy


class NoDiscountStrategy(DiscountStrategy):
    def apply(self, total: Money) -> Money:
        return total