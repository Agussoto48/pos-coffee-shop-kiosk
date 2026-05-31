from __future__ import annotations
from datetime import datetime
from pos_coffee_shop_kiosk.application.dtos.product_details import ProductDetails
from pos_coffee_shop_kiosk.domain.interfaces.abstract_product_repository import AbstractProductRepository
from pos_coffee_shop_kiosk.domain.models.value_objects.sku import Sku

class FindProduct:
    def __init__(
        self,
        product_repository: AbstractProductRepository,
    ) -> None:
        self.product_repository = product_repository

    def execute(self, product_sku: str) -> ProductDetails:
        product = self.product_repository.find_by_sku(Sku(product_sku))

        if product is None:
            raise ValueError("No se encontró un producto con ese SKU")

        return ProductDetails(
            name=str(product.name()),
            description=product.description(),
            category_name=str(product.category().name()),
            sub_category_name="",
            sku=str(product.sku()),
            price=product.price().amount(),
            final_price=product.price().amount(),
            stock=product.stock(),
            tax_options=[],
            created_at=datetime.now(),
        )
