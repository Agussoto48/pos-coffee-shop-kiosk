from __future__ import annotations


class Sku:
    _value: str

    def __init__(self, value: str) -> None:
        self._value = value
        self._validate(value)

    def _validate(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("El SKU no puede estar vacío")

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Sku) and self._value == other._value

    def __hash__(self) -> int:
        return hash(self._value)

    def __str__(self) -> str:
        return self._value

    def value(self) -> str:
        return self._value
    
    def to_dict(self):
        return {"__type__": "Sku", "value": self._value}
    
    @classmethod
    def from_dict(cls, dict):
        return cls(dict["value"])