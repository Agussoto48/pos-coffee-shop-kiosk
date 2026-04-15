from __future__ import annotations

class BrowseMenuUseCases:
    def __init__(
        self,
        fetch_product_menu: FetchProductMenu,
    ) -> None:
        self.fetch_product_menu = fetch_product_menu
