from __future__ import annotations
from pos_coffee_shop_kiosk.application.dtos.shopping_cart_summary import (CartItemSummary, ShoppingCartSummary,)
from pos_coffee_shop_kiosk.domain.models.shopping_cart import ShoppingCart

class FetchCartSummary:
    def __init__(
        self,
        shopping_cart: ShoppingCart,
    ) -> None:
        self.shopping_cart = shopping_cart

    def execute(self) -> ShoppingCartSummary:
        items = [
            CartItemSummary(
                product_name=str(item.product().name()),
                sku=str(item.product().sku()),
                quantity=item.quantity(),
                unit_price=str(item.product().price()),
                subtotal=str(item.get_subtotal()),
            )
            for item in self.shopping_cart.items()
        ]

        total = "0"

        if not self.shopping_cart.is_empty():
            total = str(self.shopping_cart.get_total())

        return ShoppingCartSummary(
            items=items,
            item_count=self.shopping_cart.get_item_count(),
            subtotal=total,
            tax_amount="0",
            total=total,
            is_empty=self.shopping_cart.is_empty(),
        )
