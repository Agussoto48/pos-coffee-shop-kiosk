from __future__ import annotations
from pos_coffee_shop_kiosk.domain.interfaces.abstract_product_repository import AbstractProductRepository
from pos_coffee_shop_kiosk.domain.models.entities.product import Product
from pos_coffee_shop_kiosk.domain.models.value_objects.sku import Sku
from pos_coffee_shop_kiosk.domain.models.value_objects.product_category import ProductCategory


class JsonProductRepository(AbstractProductRepository):

    def add(self, product: Product) -> None:
        pass

    def remove(self, product: Product) -> None:
        pass

    def find_by_sku(self, product_sku: Sku) -> Product | None:
        pass

    def fetch_products_by_category(self, category: ProductCategory) -> list[Product]:
        pass