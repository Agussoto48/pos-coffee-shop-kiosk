from __future__ import annotations
from decimal import Decimal
from uuid import uuid4
from pos_coffee_shop_kiosk.domain.enums.payment_method_type import PaymentMethodType
from pos_coffee_shop_kiosk.domain.factories.abstract_sale_factory import AbstractSaleFactory
from pos_coffee_shop_kiosk.domain.interfaces.abstract_payment_method import AbstractPaymentMethod
from pos_coffee_shop_kiosk.domain.interfaces.abstract_product_repository import AbstractProductRepository
from pos_coffee_shop_kiosk.domain.interfaces.abstract_sale_repository import AbstractSaleRepository
from pos_coffee_shop_kiosk.domain.models.entities.sale import Sale
from pos_coffee_shop_kiosk.domain.models.shopping_cart import ShoppingCart
from pos_coffee_shop_kiosk.domain.observers.sale_event_publisher import SaleEventPublisher
from pos_coffee_shop_kiosk.domain.strategies.discount_strategy import DiscountStrategy


class ProcessCheckout:
    def __init__(
        self,
        product_repository: AbstractProductRepository,
        sale_repository: AbstractSaleRepository,
        shopping_cart: ShoppingCart,
        sale_factory: AbstractSaleFactory,
        discount_strategy: DiscountStrategy,
        event_publisher: SaleEventPublisher,
    ) -> None:
        self.product_repository = product_repository
        self.sale_repository = sale_repository
        self.shopping_cart = shopping_cart
        self.sale_factory = sale_factory
        self.discount_strategy = discount_strategy
        self.event_publisher = event_publisher

    def execute(
        self,
        payment_method_type: PaymentMethodType,
        payment_method: AbstractPaymentMethod,
    ) -> Sale:
        if self.shopping_cart.is_empty():
            raise ValueError("No se puede procesar una venta con el carrito vacío")

        subtotal = self.shopping_cart.get_total()
        total_with_discount = self.discount_strategy.apply(subtotal)

        sale = self.sale_factory.create(
            sale_id=uuid4(),
            cart=self.shopping_cart,
            payment_method=payment_method_type,
            amount_paid=total_with_discount,
        )

        try:
            payment_method.pay(total_with_discount)

            for item in self.shopping_cart.items():
                product = item.product()
                product.remove_stock(Decimal(item.quantity()))
                self.product_repository.update(product)

            sale.complete()
            self.sale_repository.add(sale)
            self.event_publisher.notify(sale)
            self.shopping_cart.clear()

            return sale

        except Exception:
            sale.fail()
            self.sale_repository.add(sale)
            raise