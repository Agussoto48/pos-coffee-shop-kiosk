from __future__ import annotations
import json
from pos_coffee_shop_kiosk.infrastructure.repositories import json_encoder_decoder
from pos_coffee_shop_kiosk.domain.interfaces.abstract_product_repository import AbstractProductRepository
from pos_coffee_shop_kiosk.domain.models.entities.product import Product
from pos_coffee_shop_kiosk.domain.models.value_objects.sku import Sku
from pos_coffee_shop_kiosk.domain.models.value_objects.product_category import ProductCategory


class JsonProductRepository(AbstractProductRepository):
    _filename:str = ""

    def __init__(self, filename: str) -> None:
        self._filename = filename
        try:
            with open(self._filename) as f:
                products: list[Product] = \
                    json.load(f, object_hook=json_encoder_decoder.decode)
                self._products = {p.sku() : p for p in products}
        except FileNotFoundError:
            with open(self._filename, "w") as f:
                json.dump([], f)
            self._products: dict[Sku, Product] = {}

    def _save(self) -> None:
        with open(self._filename, "w") as f:
            json.dump(list(self._products.values()), f,\
                      default=json_encoder_decoder.encode)

    def add(self, product: Product) -> None:
        if product.sku() in self._products:
            raise ValueError("Ya existe un producto con ese SKU")
        
        self._products[product.sku()] = product
        self._save()

    def remove(self, product: Product) -> None:
        self._products.pop(product.sku(), None)
        self._save()

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
    
    def update(self, product: Product) -> None:
        if product.sku() not in self._products:
            raise ValueError("No existe un producto con ese SKU")

        self._products[product.sku()] = product
        self._save()