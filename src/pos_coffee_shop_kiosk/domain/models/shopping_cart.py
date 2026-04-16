from __future__ import annotations
from uuid import UUID
from pos_coffee_shop_kiosk.domain.models.dtos.cart_item import CartItem
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money


class ShoppingCart:
    _items: list[CartItem]

    def __init__(self, items: list[CartItem] | None = None) -> None:
        self._items = items if items is not None else []

    def add(self, item: CartItem) -> None:
        pass

    def remove(self, product_id: UUID, quantity: int) -> None:
        pass

    def clear(self) -> None:
        pass

    def get_total(self) -> Money:
        pass

    def get_item_count(self) -> int:
        pass

    def is_empty(self) -> bool:
        pass

    def find_item(self, product_id: UUID) -> CartItem | None:
        pass

    def items(self) -> list[CartItem]:
        pass