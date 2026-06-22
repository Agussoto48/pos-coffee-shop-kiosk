from __future__ import annotations
from decimal import Decimal


class Percentage:
    _value: Decimal

    def __init__(self, percentage: Decimal) -> None:
        self._value = percentage

    def _validate(self, percentage: Decimal) -> None:
        if (percentage < 0 or percentage > 100):
            raise ValueError("Percentage cannot be out of bounds [0, 100]")

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Percentage) and self._value == other._value

    def __hash__(self) -> int:
        return self._value.__hash__()

    def __str__(self) -> str:
        return self._value.__str__()

    def value(self) -> Decimal:
        return self._value