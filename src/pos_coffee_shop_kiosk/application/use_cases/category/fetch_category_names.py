from __future__ import annotations

class FetchCategoryNames:
    def __init__(
        self,
        product_category_repository: AbstractProductCategoryRepository,
    ) -> None:
        self.product_category_repository = product_category_repository

    def execute(self) -> list[str]:
        pass
