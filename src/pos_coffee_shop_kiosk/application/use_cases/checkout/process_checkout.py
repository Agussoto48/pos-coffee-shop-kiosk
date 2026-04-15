from __future__ import annotations

class ProcessCheckout:
    def __init__(
        self,
        product_repository: AbstractProductRepository,
        sale_repository: AbstractSaleRepository,
        shopping_cart: ShoppingCart,
    ) -> None:
        self.product_repository = product_repository
        self.sale_repository = sale_repository
        self.shopping_cart = shopping_cart

    def execute(
        self,
        paymentMethod: AbstractPaymentMethod,
        paymentRequest: PaymentRequest,
    ) -> Sale:
        pass
