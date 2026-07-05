from __future__ import annotations
from pos_coffee_shop_kiosk.domain.models.shopping_cart import ShoppingCart

class ClearCart:
    def __init__(
        self,
        shopping_cart: ShoppingCart,
    ) -> None:
        self.shopping_cart = shopping_cart

    def execute(self) -> None:
        self.shopping_cart.clear()
