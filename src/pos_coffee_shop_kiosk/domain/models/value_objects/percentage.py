from __future__ import annotations
from decimal import Decimal


class Percentage:
    _value: Decimal

    def __init__(self, percentage: Decimal) -> None:
        self._value = percentage

    def _validate(self, percentage: Decimal) -> None:
        pass

    def __eq__(self, other: Percentage) -> bool:
        pass

    def __hash__(self) -> int:
        pass

    def __str__(self) -> str:
        pass

    def value(self) -> Decimal:
        pass