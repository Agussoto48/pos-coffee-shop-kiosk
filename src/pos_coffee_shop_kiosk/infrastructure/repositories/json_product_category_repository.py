from __future__ import annotations
import json
from pos_coffee_shop_kiosk.infrastructure.repositories import json_encoder_decoder
from pos_coffee_shop_kiosk.domain.interfaces.abstract_product_category_repository import AbstractProductCategoryRepository
from pos_coffee_shop_kiosk.domain.models.value_objects.product_category import ProductCategory
from pos_coffee_shop_kiosk.domain.models.value_objects.category_name import CategoryName


class JsonProductCategoryRepository(AbstractProductCategoryRepository):
    __FILE_PATH: str = "categories.json"

    def __init__(self) -> None:
        try:
            with open(JsonProductCategoryRepository.__FILE_PATH) as f:
                categories: list[ProductCategory] = \
                    json.load(f, object_hook=json_encoder_decoder.decode)
                self._categories = {c.name() : c for c in categories}
        except FileNotFoundError:
            with open(JsonProductCategoryRepository.__FILE_PATH, "w") as f:
                json.dump([], f)
            self._categories: dict[CategoryName, ProductCategory] = {}
    
    def _save(self) -> None:
        with open(JsonProductCategoryRepository.__FILE_PATH, "w") as f:
            json.dump(list(self._categories.values()), f,\
                      default=json_encoder_decoder.encode)

    def add(self, category: ProductCategory) -> None:
        self._categories[category.name()] = category
        self._save()

    def remove(self, category: ProductCategory) -> None:
        self._categories.pop(category.name(), None)
        self._save()

    def find_by_name(self, name: CategoryName) -> ProductCategory | None:
        return self._categories.get(name)

    def fetch_all_categories(self) -> list[ProductCategory]:
        return list(self._categories.values())