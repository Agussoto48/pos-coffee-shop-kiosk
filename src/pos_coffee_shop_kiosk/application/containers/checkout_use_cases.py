from __future__ import annotations
from pos_coffee_shop_kiosk.application.use_cases.checkout.process_checkout import ProcessCheckout
from pos_coffee_shop_kiosk.application.use_cases.checkout.create_payment_method import CreatePaymentMethod


class CheckoutUseCases:
    def __init__(
        self,
        process_checkout: ProcessCheckout,
        create_payment_method: CreatePaymentMethod,
    ) -> None:
        self.process_checkout = process_checkout
        self.create_payment_method = create_payment_method