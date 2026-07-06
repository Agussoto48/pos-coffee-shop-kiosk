from __future__ import annotations

from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.strategies.discount_strategy import DiscountStrategy


class FixedAmountDiscountStrategy(DiscountStrategy):
    def __init__(self, discount: Money) -> None:
        if discount.amount() < 0:
            raise ValueError("El descuento no puede ser negativo")

        self._discount = discount

    def apply(self, total: Money) -> Money:
        if self._discount.currency() != total.currency():
            raise ValueError("La moneda del descuento no coincide con la moneda del total")

        final_amount = total.amount() - self._discount.amount()

        if final_amount < 0:
            final_amount = 0

        return Money(final_amount, total.currency())