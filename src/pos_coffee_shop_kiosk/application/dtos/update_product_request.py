from __future__ import annotations
from decimal import Decimal


class UpdateProductRequest:
    sku: str
    name: str | None
    price: Decimal | None
    category_name: str | None
    sub_category_name: str | None
    tax_options: list[str] | None

    def __init__(
        self,
        sku: str,
        name: str | None = None,
        price: Decimal | None = None,
        category_name: str | None = None,
        sub_category_name: str | None = None,
        tax_options: list[str] | None = None,
    ) -> None:
        self.sku = sku
        self.name = name
        self.price = price
        self.category_name = category_name
        self.sub_category_name = sub_category_name
        self.tax_options = tax_options