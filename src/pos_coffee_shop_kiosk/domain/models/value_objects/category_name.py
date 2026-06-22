from __future__ import annotations

class CategoryName:
    def __init__(self, name: str) -> None:
        self._value = name
        self._validate(name)

    def _validate(self, name: str) -> None:
        if not name or not name.strip():
            raise ValueError("El nombre de la categoría no puede estar vacío")

    def __eq__(self, other: object) -> bool:
        return isinstance(other, CategoryName) and self._value == other._value

    def __hash__(self) -> int:
        return hash(self._value)

    def __str__(self) -> str:
        return self._value

    def value(self) -> str:
        return self._value

    def to_dict(self):
        return {"__type__": "CategoryName", "value": self._value}
    
    @classmethod
    def from_dict(cls, dict):
        return cls(dict["value"])