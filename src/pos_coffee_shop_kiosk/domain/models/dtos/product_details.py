from __future__ import annotations
from decimal import Decimal
from datetime import datetime

class ProductDetails:
    name: str
    description: str
    category_name: str
    sub_category_name: str
    sku: str
    price: Decimal
    final_price: Decimal
    stock: Decimal
    tax_options: list[str]
    created_at: datetime

    def __init__(
        self,
        name: str,
        description: str,
        category_name: str,
        sub_category_name: str,
        sku: str,
        price: Decimal,
        final_price: Decimal,
        stock: Decimal,
        tax_options: list[str],
        created_at: datetime,
    ) -> None:
        self.name = name
        self.description = description
        self.category_name = category_name
        self.sub_category_name = sub_category_name
        self.sku = sku
        self.price = price
        self.final_price = final_price
        self.stock = stock
        self.tax_options = tax_options
        self.created_at = created_at