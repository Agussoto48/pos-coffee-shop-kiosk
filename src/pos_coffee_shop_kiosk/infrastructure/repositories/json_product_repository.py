from __future__ import annotations
from pos_coffee_shop_kiosk.domain.interfaces.abstract_product_repository import AbstractProductRepository
from pos_coffee_shop_kiosk.domain.models.entities.product import Product
from pos_coffee_shop_kiosk.domain.models.value_objects.sku import Sku
from pos_coffee_shop_kiosk.domain.models.value_objects.product_category import ProductCategory


class JsonProductRepository(AbstractProductRepository):
    def __init__(self) -> None:
        self._products: dict[Sku, Product] = {}
    
    def add(self, product: Product) -> None:
        if product.sku() in self._products:
            raise ValueError("Ya existe un producto con ese SKU")
        
        self._products[product.sku()] = product

    def remove(self, product: Product) -> None:
        self._products.pop(product.sku(), None)

    def find_by_sku(self, product_sku: Sku) -> Product | None:
        return self._products.get(product_sku)

    def fetch_products_by_category(self, category: ProductCategory) -> list[Product]:
        return [
            product
            for product in self._products.values()
            if product.category() == category
        ]
    
    def fetch_all_products(self) -> list[Product]:
        return list(self._products.values())