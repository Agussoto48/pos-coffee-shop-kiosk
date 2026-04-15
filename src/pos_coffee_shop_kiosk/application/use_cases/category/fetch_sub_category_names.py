from __future__ import annotations

class FetchSubCategoryNames:
    def __init__(
        self,
        product_category_repository: AbstractProductCategoryRepository,
    ) -> None:
        self.product_category_repository = product_category_repository

    def execute(self, parent_category_name: str) -> list[str]:
        pass
