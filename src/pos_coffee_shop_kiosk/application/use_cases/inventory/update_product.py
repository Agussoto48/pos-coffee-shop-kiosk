from __future__ import annotations
from decimal import Decimal

from pos_coffee_shop_kiosk.domain.enums.currency import Currency
from pos_coffee_shop_kiosk.domain.interfaces.abstract_product_repository import AbstractProductRepository
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.models.value_objects.sku import Sku

class UpdateProduct:
    def __init__(
        self,
        product_repository: AbstractProductRepository,
    ) -> None:
        self.product_repository = product_repository
        
    def execute(
        self,
        product_sku: str,
        new_price: Decimal | None = None,
        stock_to_add: Decimal | None = None,
        stock_to_remove: Decimal | None = None,
    ) -> None:
        
        product = self.product_repository.find_by_sku(Sku(product_sku))
        if product is None:
            raise ValueError("No se encontró un producto con ese SKU")

        if new_price is not None:
            product.update_price(Money(new_price, Currency.COLONES))

        if stock_to_add is not None:
            product.add_stock(stock_to_add)

        if stock_to_remove is not None:
            product.remove_stock(stock_to_remove)
        
        self.product_repository.update(product)
        
