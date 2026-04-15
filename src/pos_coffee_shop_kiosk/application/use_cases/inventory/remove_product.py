from __future__ import annotations

class RemoveProduct:
    def __init__(
        self,
        product_repository: AbstractProductRepository,
    ) -> None:
        self.product_repository = product_repository

    def execute(self, product_sku: str) -> None:
        pass
