from __future__ import annotations
from pos_coffee_shop_kiosk.domain.models.value_objects.category_name import CategoryName


class ProductCategory:
    _name: CategoryName
    _parent: ProductCategory | None

    def __init__(self, name: str, parent: ProductCategory | None) -> None:
        self._name = CategoryName(name)
        self._parent = parent

    def _validate(self, name: str) -> None:
        pass

    def __eq__(self, other: ProductCategory) -> bool:
        pass

    def __hash__(self) -> int:
        pass

    def __str__(self) -> str:
        pass

    def name(self) -> CategoryName:
        pass

    def parent(self) -> ProductCategory | None:
        pass