from __future__ import annotations


class Sku:
    _value: str

    def __init__(self, value: str) -> None:
        self._value = value

    def _validate(self, value: str) -> None:
        pass

    def __eq__(self, other: Sku) -> bool:
        pass

    def __hash__(self) -> int:
        pass

    def __str__(self) -> str:
        pass

    def value(self) -> str:
        pass