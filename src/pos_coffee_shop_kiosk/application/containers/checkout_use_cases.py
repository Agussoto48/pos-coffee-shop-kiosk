from __future__ import annotations

class CheckoutUseCases:
    def __init__(
        self,
        process_checkout: ProcessCheckout,
        create_payment_method: CreatePaymentMethod,
    ) -> None:
        self.process_checkout = process_checkout
        self.create_payment_method = create_payment_method
