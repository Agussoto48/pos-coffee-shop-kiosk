from __future__ import annotations
from decimal import Decimal

from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.strategies.discount_strategy import DiscountStrategy


class PercentageDiscountStrategy(DiscountStrategy):
    def __init__(self, percentage: Decimal) -> None:
        if percentage < 0 or percentage > 100:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100")

        self._percentage = percentage

    def apply(self, total: Money) -> Money:
        discount_amount = total.amount() * (self._percentage / Decimal("100"))
        return Money(total.amount() - discount_amount, total.currency())