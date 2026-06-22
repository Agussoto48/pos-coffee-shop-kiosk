from __future__ import annotations
from decimal import Decimal
from uuid import UUID
from typing import cast

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

    # Metodos para Actualizar

    def update_price(self, new_price: Money) -> None:
        self._price = new_price

    def add_stock(self, amount: Decimal) -> None:
        if amount <= 0:
            raise ValueError("La cantidad a agregar debe ser mayor que cero")

        if self._stock is None:
            self._stock = amount
        else:
            self._stock += amount

    def remove_stock(self, amount: Decimal) -> None:
        if amount <= 0:
            raise ValueError("La cantidad a remover debe ser mayor que cero")
        
        if self._stock is None:
            raise ValueError("Stock no definido")

        if self._stock < amount:
            raise ValueError("Stock insuficiente")

        self._stock -= amount

    #Gets

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

    def to_dict(self) -> dict[str, object]:
        return {
            "__type__": "Product",
            "id": str(self._id),
            "name": self._name.to_dict(),
            "description": self._description,
            "category": self._category.to_dict(),
            "sku": self._sku.to_dict(),
            "price": self._price.to_dict(),
            "stock": str(self._stock) if self._stock is not None else None,
            "tax_options": [t.to_dict() for t in self._tax_options],
        }

    @classmethod
    def from_dict(cls, d: dict[str, object]) -> Product:
        return cls(
            id=UUID(str(d["id"])),
            name=cast(ProductName, d["name"]),
            description=str(d["description"]),
            category=cast(ProductCategory, d["category"]),
            sku=cast(Sku, d["sku"]),
            price=cast(Money, d["price"]),
            stock=Decimal(str(d["stock"])) if d.get("stock") is not None else None,
            tax_options=cast(list[TaxOption], d["tax_options"]),
        )
