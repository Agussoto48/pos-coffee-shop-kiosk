from __future__ import annotations
from typing import cast
from pos_coffee_shop_kiosk.domain.models.value_objects.category_name import CategoryName


class ProductCategory:
    _name: CategoryName
    _parent: ProductCategory | None

    def __init__(self, name: str, parent: ProductCategory | None) -> None:
        self._validate(name)
        self._name = CategoryName(name)
        self._parent = parent

    def _validate(self, name: str) -> None:
        if not name or not name.strip():
            raise ValueError("El nombre de la categoría no puede estar vacío")

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, ProductCategory)
            and self._name == other._name
            and self._parent == other._parent
        )

    def __hash__(self) -> int:
        return hash((self._name, self._parent))

    def __str__(self) -> str:
        if self._parent is None:
            return str(self._name)
        return f"{self._parent} / {self._name}"

    def name(self) -> CategoryName:
        return self._name

    def parent(self) -> ProductCategory | None:
        return self._parent
    
    def to_dict(self) -> dict[str, str | object]:
        return {
            "__type__": "ProductCategory",
            "name": self._name.value(),
            "parent": self._parent.to_dict()\
                                    if self._parent is not None else None
        }

    @classmethod
    def from_dict(cls, d : dict[str, str | object]) -> ProductCategory:
        parent = cast(ProductCategory | None, d.get("parent")) 
        return cls(name=str(d["name"]), parent=parent)