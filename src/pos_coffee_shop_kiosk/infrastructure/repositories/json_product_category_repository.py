from __future__ import annotations
from pos_coffee_shop_kiosk.domain.interfaces.abstract_product_category_repository import AbstractProductCategoryRepository
from pos_coffee_shop_kiosk.domain.models.value_objects.product_category import ProductCategory
from pos_coffee_shop_kiosk.domain.models.value_objects.category_name import CategoryName


class JsonProductCategoryRepository(AbstractProductCategoryRepository):

    def __init__(self) -> None:
        self._categories: dict[CategoryName, ProductCategory] = {}
    
    def add(self, category: ProductCategory) -> None:
        self._categories[category.name()] = category

    def remove(self, category: ProductCategory) -> None:
        self._categories.pop(category.name(), None)

    def find_by_name(self, name: CategoryName) -> ProductCategory | None:
        return self._categories.get(name)

    def fetch_all_categories(self) -> list[ProductCategory]:
        return list(self._categories.values())