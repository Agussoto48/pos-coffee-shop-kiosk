from __future__ import annotations

class FetchProductMenu:
    def __init__(
        self,
        product_repository: AbstractProductRepository,
        product_category_repository: AbstractProductCategoryRepository,
    ) -> None:
        self.product_repository = product_repository
        self.product_category_repository = product_category_repository

    def execute(self) -> list[ProductDetails]:
        pass
