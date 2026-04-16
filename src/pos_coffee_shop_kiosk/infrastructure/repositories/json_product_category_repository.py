from __future__ import annotations
from pos_coffee_shop_kiosk.domain.interfaces.abstract_product_category_repository import AbstractProductCategoryRepository
from pos_coffee_shop_kiosk.domain.models.value_objects.product_category import ProductCategory
from pos_coffee_shop_kiosk.domain.models.value_objects.category_name import CategoryName


class JsonProductCategoryRepository(AbstractProductCategoryRepository):

    def add(self, category: ProductCategory) -> None:
        pass

    def remove(self, category: ProductCategory) -> None:
        pass

    def find_by_name(self, name: CategoryName) -> ProductCategory | None:
        pass

    def fetch_all_categories(self) -> list[ProductCategory]:
        pass