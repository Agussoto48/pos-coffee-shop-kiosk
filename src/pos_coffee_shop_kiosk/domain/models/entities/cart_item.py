from __future__ import annotations
from pos_coffee_shop_kiosk.domain.models.entities.product import Product
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money


class CartItem:
    _product: Product
    _quantity: int

    def __init__(self, product: Product, quantity: int) -> None:
        self._product = product
        self._quantity = quantity

    def update_quantity(self, quantity: int) -> None:
        pass

    def get_subtotal(self) -> Money:
        pass

    def product(self) -> Product:
        pass

    def quantity(self) -> int:
        pass