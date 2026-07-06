from __future__ import annotations
from decimal import Decimal
from pos_coffee_shop_kiosk.application.containers.checkout_use_cases import CheckoutUseCases
from pos_coffee_shop_kiosk.application.containers.kiosk_app_use_cases import KioskAppUseCases
from pos_coffee_shop_kiosk.application.containers.shopping_cart_use_cases import ShoppingCartUseCases
from pos_coffee_shop_kiosk.application.use_cases.checkout.create_payment_method import CreatePaymentMethod
from pos_coffee_shop_kiosk.application.use_cases.checkout.process_checkout import ProcessCheckout
from pos_coffee_shop_kiosk.application.use_cases.shopping_cart.add_cart_item import AddCartItem
from pos_coffee_shop_kiosk.application.use_cases.shopping_cart.remove_cart_item import RemoveCartItem
from pos_coffee_shop_kiosk.application.use_cases.shopping_cart.clear_cart import ClearCart
from pos_coffee_shop_kiosk.application.use_cases.shopping_cart.fetch_cart_summary import FetchCartSummary
from pos_coffee_shop_kiosk.domain.factories.physical_sale_factory import PhysicalSaleFactory
from pos_coffee_shop_kiosk.domain.models.shopping_cart import ShoppingCart
from pos_coffee_shop_kiosk.domain.observers.sale_event_publisher import SaleEventPublisher
from pos_coffee_shop_kiosk.domain.observers.inventory_sale_observer import InventorySaleObserver
from pos_coffee_shop_kiosk.domain.observers.report_sale_observer import ReportSaleObserver
from pos_coffee_shop_kiosk.domain.observers.receipt_sale_observer import ReceiptSaleObserver
from pos_coffee_shop_kiosk.domain.strategies.percentage_discount_strategy import PercentageDiscountStrategy
from pos_coffee_shop_kiosk.infrastructure.factories.basic_payment_method_factory import BasicPaymentMethodFactory
from pos_coffee_shop_kiosk.infrastructure.repositories.json_product_repository import JsonProductRepository
from pos_coffee_shop_kiosk.infrastructure.repositories.json_sale_repository import JsonSaleRepository
from pos_coffee_shop_kiosk.application.use_cases.inventory.list_products import ListProducts


def create_kiosk_use_cases(branch: str = "san_jose") -> KioskAppUseCases:
    product_repository = JsonProductRepository(f"{branch}_db.json")
    sale_repository = JsonSaleRepository()
    shopping_cart = ShoppingCart()

    event_publisher = SaleEventPublisher()
    event_publisher.subscribe(InventorySaleObserver())
    event_publisher.subscribe(ReportSaleObserver())
    event_publisher.subscribe(ReceiptSaleObserver())

    shopping_cart_use_cases = ShoppingCartUseCases(
        add_cart_item=AddCartItem(product_repository, shopping_cart),
        remove_cart_item=RemoveCartItem(product_repository, shopping_cart),
        clear_cart=ClearCart(shopping_cart),
        fetch_cart_summary=FetchCartSummary(shopping_cart),
    )

    checkout_use_cases = CheckoutUseCases(
        process_checkout=ProcessCheckout(
            product_repository=product_repository,
            sale_repository=sale_repository,
            shopping_cart=shopping_cart,
            sale_factory=PhysicalSaleFactory(),
            discount_strategy=PercentageDiscountStrategy(Decimal("10")),
            event_publisher=event_publisher,
        ),
        create_payment_method=CreatePaymentMethod(
            BasicPaymentMethodFactory()
        ),
    )

    return KioskAppUseCases(
        browse_menu=ListProducts(product_repository),
        shopping_cart=shopping_cart_use_cases,
        checkout=checkout_use_cases,
    )


def create_admin_use_cases():
    raise NotImplementedError("La aplicación administrativa no está conectada todavía.")