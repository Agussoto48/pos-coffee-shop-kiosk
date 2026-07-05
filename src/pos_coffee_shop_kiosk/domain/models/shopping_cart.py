from __future__ import annotations
from uuid import UUID
from pos_coffee_shop_kiosk.domain.models.entities.cart_item import CartItem
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money


class ShoppingCart:
    _items: list[CartItem]

    def __init__(self, items: list[CartItem] | None = None) -> None:
        self._items = items if items is not None else []

    def add(self, item: CartItem) -> None:
        existing_item = self.find_item(item.product().id())
        if existing_item is None:
            self._items.append(item)
        else:
            new_quantity = existing_item.quantity() + item.quantity()
            existing_item.update_quantity(new_quantity)

    def remove(self, product_id: UUID, quantity: int) -> None:
        item = self.find_item(product_id)

        if item is None:
            raise ValueError("El producto no está en el carrito")

        if quantity <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        if quantity > item.quantity():
            raise ValueError("No se puede remover más cantidad de la existente en el carrito")

        new_quantity = item.quantity() - quantity

        if new_quantity == 0:
            self._items.remove(item)
        else:
            item.update_quantity(new_quantity)

    def clear(self) -> None:
        self._items.clear()

    def get_total(self) -> Money:
        if self.is_empty():
            raise ValueError("El carrito está vacío")
        
        total = self._items[0].get_subtotal()
        for item in self._items[1:]:
            total = total.add(item.get_subtotal())
        
        return total

    def get_item_count(self) -> int:
        return sum(item.quantity() for item in self._items)

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def find_item(self, product_id: UUID) -> CartItem | None:
        for item in self._items:
            if item.product().id() == product_id:
                return item

        return None

    def items(self) -> list[CartItem]:
        return list(self._items)