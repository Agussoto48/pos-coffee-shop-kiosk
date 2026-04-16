from __future__ import annotations


class ProductName:
    _value: str

    def __init__(self, name: str) -> None:
        self._value = name

    def _validate(self, name: str) -> None:
        pass

    def __eq__(self, other: ProductName) -> bool:
        pass

    def __hash__(self) -> int:
        pass

    def __str__(self) -> str:
        pass

    def value(self) -> str:
        pass