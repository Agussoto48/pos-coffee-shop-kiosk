from __future__ import annotations
from abc import ABC, abstractmethod
from pos_coffee_shop_kiosk.domain.models.entities.product import Product
from pos_coffee_shop_kiosk.domain.models.value_objects.sku import Sku
from pos_coffee_shop_kiosk.domain.models.value_objects.product_category import ProductCategory


class AbstractProductRepository(ABC):

    @abstractmethod
    def add(self, product: Product) -> None:
        pass

    @abstractmethod
    def remove(self, product: Product) -> None:
        pass

    @abstractmethod
    def find_by_sku(self, product_sku: Sku) -> Product | None:
        pass

    @abstractmethod
    def fetch_products_by_category(self, category: ProductCategory) -> list[Product]:
        pass