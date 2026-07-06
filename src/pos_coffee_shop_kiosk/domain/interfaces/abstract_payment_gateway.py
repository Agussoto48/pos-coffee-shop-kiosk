from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Mapping

from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money


@dataclass(frozen=True)
class PaymentGatewayResult:
    approved: bool
    transaction_id: str | None
    message: str


class AbstractPaymentGateway(ABC):
    """Puerto estable utilizado por la aplicación para cobrar una venta."""

    @abstractmethod
    def charge(
        self,
        amount: Money,
        payment_data: Mapping[str, str],
    ) -> PaymentGatewayResult:
        raise NotImplementedError
