from __future__ import annotations

class ProductInventoryUseCases:
    def __init__(
        self,
        register_product: RegisterProduct,
        remove_product: RemoveProduct,
        update_product: UpdateProduct,
        find_product: FindProduct,
    ) -> None:
        self.register_product = register_product
        self.remove_product = remove_product
        self.update_product = update_product
        self.find_product = find_product
