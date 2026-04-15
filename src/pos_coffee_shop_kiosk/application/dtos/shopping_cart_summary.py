from __future__ import annotations

class ShoppingCartSummary:
    items: list[CartItemSummary]
    item_count: int
    subtotal: str
    tax_amount: str
    total: str
    is_empty: bool

    def __init__(
        self,
        items: list[CartItemSummary],
        item_count: int,
        subtotal: str,
        tax_amount: str,
        total: str,
        is_empty: bool,
    ) -> None:
        self.items = items
        self.item_count = item_count
        self.subtotal = subtotal
        self.tax_amount = tax_amount
        self.total = total
        self.is_empty = is_empty


class CartItemSummary:
    product_name: str
    sku: str
    quantity: int
    unit_price: str
    subtotal: str

    def __init__(
        self,
        product_name: str,
        sku: str,
        quantity: int,
        unit_price: str,
        subtotal: str,
    ) -> None:
        self.product_name = product_name
        self.sku = sku
        self.quantity = quantity
        self.unit_price = unit_price
        self.subtotal = subtotal
