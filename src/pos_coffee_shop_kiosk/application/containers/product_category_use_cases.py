from __future__ import annotations

class ProductCategoryUseCases:
    def __init__(
        self,
        add_category: AddCategory,
        remove_category: RemoveCategory,
        add_sub_category: AddSubCategory,
        remove_sub_category: RemoveSubCategory,
        fetch_category_names: FetchCategoryNames,
        fetch_sub_category_names: FetchSubCategoryNames,
    ) -> None:
        self.add_category = add_category
        self.remove_category = remove_category
        self.add_sub_category = add_sub_category
        self.remove_sub_category = remove_sub_category
        self.fetch_category_names = fetch_category_names
        self.fetch_sub_category_names = fetch_sub_category_names
