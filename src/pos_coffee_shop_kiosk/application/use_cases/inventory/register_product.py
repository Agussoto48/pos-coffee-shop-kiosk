from __future__ import annotations
from uuid import uuid4

from pos_coffee_shop_kiosk.application.dtos.register_product_request import RegisterProductRequest
from pos_coffee_shop_kiosk.domain.enums.currency import Currency
from pos_coffee_shop_kiosk.domain.interfaces.abstract_product_category_repository import AbstractProductCategoryRepository
from pos_coffee_shop_kiosk.domain.interfaces.abstract_product_repository import AbstractProductRepository
from pos_coffee_shop_kiosk.domain.interfaces.abstract_tax_option_repository import AbstractTaxOptionRepository
from pos_coffee_shop_kiosk.domain.models.entities.product import Product
from pos_coffee_shop_kiosk.domain.models.value_objects.category_name import CategoryName
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.models.value_objects.product_category import ProductCategory
from pos_coffee_shop_kiosk.domain.models.value_objects.product_name import ProductName
from pos_coffee_shop_kiosk.domain.models.value_objects.sku import Sku
from pos_coffee_shop_kiosk.domain.models.value_objects.tax_description import TaxDescription

class RegisterProduct:
    def __init__(
        self,
        product_repository: AbstractProductRepository,
        product_category_repository: AbstractProductCategoryRepository,
        tax_option_repository: AbstractTaxOptionRepository,
    ) -> None:
        self.product_repository = product_repository
        self.product_category_repository = product_category_repository
        self.tax_option_repository = tax_option_repository

    def execute(self, request: RegisterProductRequest) -> None:
        sku = Sku(request.sku)

        existing_product = self.product_repository.find_by_sku(sku)

        if existing_product is not None:
            raise ValueError("Ya existe un producto con ese SKU")

        category = self.product_category_repository.find_by_name(
            CategoryName(request.category_name)
        )

        if category is None:
            category = ProductCategory(request.category_name, None)

        tax_options = []

        for tax_description in request.tax_options:
            tax_option = self.tax_option_repository.find_by_description(
                TaxDescription(tax_description)
            )

            if tax_option is not None:
                tax_options.append(tax_option)

        product = Product(
            id=uuid4(),
            name=ProductName(request.name),
            description=request.description,
            category=category,
            sku=sku,
            price=Money(request.price, Currency.COLONES),
            stock=request.stock,
            tax_options=tax_options,
        )

        self.product_repository.add(product)
