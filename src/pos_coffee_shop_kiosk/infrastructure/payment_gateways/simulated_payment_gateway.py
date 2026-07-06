from __future__ import annotations

from typing import Mapping
from uuid import uuid4

from pos_coffee_shop_kiosk.domain.interfaces.abstract_payment_gateway import (
    AbstractPaymentGateway,
    PaymentGatewayResult,
)
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money


class SimulatedPaymentGateway(AbstractPaymentGateway):
    """Pasarela local para demostraciones y pruebas, sin conexión bancaria real."""

    def charge(
        self,
        amount: Money,
        payment_data: Mapping[str, str],
    ) -> PaymentGatewayResult:
        if amount.amount() <= 0:
            return PaymentGatewayResult(False, None, "El monto debe ser mayor que cero")
        if payment_data.get("force_decline", "false").lower() == "true":
            return PaymentGatewayResult(False, None, "Pago rechazado por la pasarela")
        return PaymentGatewayResult(True, str(uuid4()), "Pago aprobado")
