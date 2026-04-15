class KioskAppUseCases:
    def __init__(
        self,
        browse_menu: BrowseMenuUseCases,
        shopping_cart: ShoppingCartUseCases,
        checkout: CheckoutUseCases,
    ) -> None:
        self.browse_menu = browse_menu
        self.shopping_cart = shopping_cart
        self.checkout = checkout
