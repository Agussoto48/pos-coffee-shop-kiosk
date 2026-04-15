from __future__ import annotations

class AddCartItem:
    def __init__(
        self,
        product_repository: AbstractProductRepository,
        shopping_cart: ShoppingCart,
    ) -> None:
        self.product_repository = product_repository
        self.shopping_cart = shopping_cart

    def execute(self, product_sku: str, quantity: int) -> None:
        pass
