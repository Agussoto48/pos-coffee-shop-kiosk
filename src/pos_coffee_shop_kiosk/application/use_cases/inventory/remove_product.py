from __future__ import annotations
from pos_coffee_shop_kiosk.domain.interfaces.abstract_product_repository import AbstractProductRepository
from pos_coffee_shop_kiosk.domain.models.value_objects.sku import Sku

class RemoveProduct:
    def __init__(
        self,
        product_repository: AbstractProductRepository,
    ) -> None:
        self.product_repository = product_repository

    def execute(self, product_sku: str) -> None:
        product = self.product_repository.find_by_sku(Sku(product_sku))

        if product is None:
            raise ValueError("No se encontró un producto con ese SKU")

        self.product_repository.remove(product)
