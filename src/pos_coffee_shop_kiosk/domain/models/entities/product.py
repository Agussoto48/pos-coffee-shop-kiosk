from __future__ import annotations
from decimal import Decimal
from uuid import UUID

from pos_coffee_shop_kiosk.domain.models.value_objects.product_name import ProductName
from pos_coffee_shop_kiosk.domain.models.value_objects.product_category import ProductCategory
from pos_coffee_shop_kiosk.domain.models.value_objects.sku import Sku
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.models.value_objects.tax_option import TaxOption


class Product:
    def __init__(
        self,
        id: UUID,
        name: ProductName,
        description: str,
        category: ProductCategory,
        sku: Sku,
        price: Money,
        stock: Decimal | None,
        tax_options: list[TaxOption],
    ) -> None:
        self._id = id
        self._name = name
        self._description = description
        self._category = category
        self._sku = sku
        self._price = price
        self._stock = stock
        self._tax_options = tax_options

    # =========================
    # MÉTODOS DE NEGOCIO
    # =========================

    def update_price(self, new_price: Money) -> None:
        self._price = new_price

    def add_stock(self, amount: Decimal) -> None:
        if self._stock is None:
            self._stock = amount
        else:
            self._stock += amount

    def remove_stock(self, amount: Decimal) -> None:
        if self._stock is None:
            raise ValueError("Stock no definido")

        if self._stock < amount:
            raise ValueError("Stock insuficiente")

        self._stock -= amount

    # =========================
    # GETTERS
    # =========================

    def id(self) -> UUID:
        return self._id

    def name(self) -> ProductName:
        return self._name

    def description(self) -> str:
        return self._description

    def category(self) -> ProductCategory:
        return self._category

    def sku(self) -> Sku:
        return self._sku

    def price(self) -> Money:
        return self._price

    def stock(self) -> Decimal | None:
        return self._stock

    def tax_options(self) -> list[TaxOption]:
        return self._tax_options