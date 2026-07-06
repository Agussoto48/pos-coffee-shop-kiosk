from __future__ import annotations
from pos_coffee_shop_kiosk.application.use_cases.shopping_cart.add_cart_item import AddCartItem
from pos_coffee_shop_kiosk.application.use_cases.shopping_cart.remove_cart_item import RemoveCartItem
from pos_coffee_shop_kiosk.application.use_cases.shopping_cart.clear_cart import ClearCart
from pos_coffee_shop_kiosk.application.use_cases.shopping_cart.fetch_cart_summary import FetchCartSummary


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