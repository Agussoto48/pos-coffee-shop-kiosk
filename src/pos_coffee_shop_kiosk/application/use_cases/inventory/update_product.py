from __future__ import annotations

class UpdateProduct:
    def __init__(
        self,
        product_repository: AbstractProductRepository,
        product_category_repository: AbstractProductCategoryRepository,
        tax_option_repository: AbstractTaxOptionRepository,
    ) -> None:
        self.product_repository = product_repository
        self.product_category_repository = product_category_repository
        self.tax_option_repository = tax_option_repository

    def execute(self, request: UpdateProductRequest) -> None:
        pass
