from __future__ import annotations

class FetchCartSummary:
    def __init__(
        self,
        shopping_cart: ShoppingCart,
    ) -> None:
        self.shopping_cart = shopping_cart

    def execute(self) -> ShoppingCartSummary:
        pass
