from __future__ import annotations
from decimal import Decimal

class RegisterProductRequest:
    name: str
    description: str
    category_name: str
    sub_category_name: str
    sku: str
    price: Decimal
    stock: Decimal
    tax_options: list[str]

    def __init__(
        self,
        name: str,
        description: str,
        category_name: str,
        sub_category_name: str,
        sku: str,
        price: Decimal,
        stock: Decimal,
        tax_options: list[str],
    ) -> None:
        self.name = name
        self.description = description
        self.category_name = category_name
        self.sub_category_name = sub_category_name
        self.sku = sku
        self.price = price
        self.stock = stock
        self.tax_options = tax_options