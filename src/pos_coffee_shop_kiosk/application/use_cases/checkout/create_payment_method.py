from __future__ import annotations

class CreatePaymentMethod:
    def __init__(
        self,
        paymentMethodFactory: AbstractPaymentMethodFactory,
    ) -> None:
        self.paymentMethodFactory = paymentMethodFactory

    def execute(
        self,
        methodType: PaymentMethodType,
        clientDetails: ClientPaymentDetails,
    ) -> AbstractPaymentMethod:
        pass
