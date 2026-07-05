from __future__ import annotations
from decimal import Decimal

from pos_coffee_shop_kiosk.domain.interfaces.abstract_product_repository import AbstractProductRepository
from pos_coffee_shop_kiosk.domain.models.entities.cart_item import CartItem
from pos_coffee_shop_kiosk.domain.models.shopping_cart import ShoppingCart
from pos_coffee_shop_kiosk.domain.models.value_objects.sku import Sku

class AddCartItem:
    def __init__(
        self,
        product_repository: AbstractProductRepository,
        shopping_cart: ShoppingCart,
    ) -> None:
        self.product_repository = product_repository
        self.shopping_cart = shopping_cart

    def execute(self, product_sku: str, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        product = self.product_repository.find_by_sku(Sku(product_sku))

        if product is None:
            raise ValueError("No se encontró un producto con ese SKU")

        if product.stock() is not None and product.stock() < Decimal(quantity):
            raise ValueError("Stock insuficiente")

        item = CartItem(product, quantity)
        self.shopping_cart.add(item)
