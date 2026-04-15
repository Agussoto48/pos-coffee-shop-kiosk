from __future__ import annotations

class ShoppingCartUseCases:
    def __init__(
        self,
        add_cart_item: AddCartItem,
        remove_cart_item: RemoveCartItem,
        clear_cart: ClearCart,
        fetch_cart_summary: FetchCartSummary,
    ) -> None:
        self.add_cart_item = add_cart_item
        self.remove_cart_item = remove_cart_item
        self.clear_cart = clear_cart
        self.fetch_cart_summary = fetch_cart_summary
