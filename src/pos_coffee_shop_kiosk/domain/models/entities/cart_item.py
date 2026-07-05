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
        if quantity <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")
        
        self._quantity = quantity

    def get_subtotal(self) -> Money:
        total_amount = self._product.price().amount() * self._quantity
        return Money(total_amount, self._product.price().currency())

    def product(self) -> Product:
        return self._product

    def quantity(self) -> int:
        return self._quantity