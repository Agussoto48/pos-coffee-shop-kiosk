from __future__ import annotations
from abc import ABC, abstractmethod
from pos_coffee_shop_kiosk.domain.models.value_objects.product_category import ProductCategory
from pos_coffee_shop_kiosk.domain.models.value_objects.category_name import CategoryName


class AbstractProductCategoryRepository(ABC):

    @abstractmethod
    def add(self, category: ProductCategory) -> None:
        pass

    @abstractmethod
    def remove(self, category: ProductCategory) -> None:
        pass

    @abstractmethod
    def find_by_name(self, name: CategoryName) -> ProductCategory | None:
        pass

    @abstractmethod
    def fetch_all_categories(self) -> list[ProductCategory]:
        pass