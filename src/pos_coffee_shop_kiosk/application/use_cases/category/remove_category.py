from __future__ import annotations

class RemoveCategory:
    def __init__(
        self,
        product_category_repository: AbstractProductCategoryRepository,
    ) -> None:
        self.product_category_repository = product_category_repository

    def execute(self, category_name: str) -> None:
        pass
