from __future__ import annotations
from typing import Any
from pos_coffee_shop_kiosk.application.containers.shopping_cart_use_cases import ShoppingCartUseCases
from pos_coffee_shop_kiosk.application.containers.checkout_use_cases import CheckoutUseCases


class KioskAppUseCases:
    def __init__(
        self,
        browse_menu: Any,
        shopping_cart: ShoppingCartUseCases,
        checkout: CheckoutUseCases,
    ) -> None:
        self.browse_menu = browse_menu
        self.shopping_cart = shopping_cart
        self.checkout = checkout