from __future__ import annotations

from datetime import datetime

from pos_coffee_shop_kiosk.application.dtos.product_details import ProductDetails
from pos_coffee_shop_kiosk.domain.interfaces.abstract_product_repository import AbstractProductRepository


class ListProducts:
    def __init__(
        self,
        product_repository: AbstractProductRepository,
    ) -> None:
        self.product_repository = product_repository

    def execute(self) -> list[ProductDetails]:
        products = self.product_repository.fetch_all_products()

        return [
            ProductDetails(
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
            for product in products
        ]