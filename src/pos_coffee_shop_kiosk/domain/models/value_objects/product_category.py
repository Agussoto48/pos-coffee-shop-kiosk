from __future__ import annotations
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

    def __eq__(self, other: ProductCategory) -> bool:
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