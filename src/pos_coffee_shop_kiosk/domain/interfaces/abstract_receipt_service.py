from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money


@dataclass(frozen=True)
class ReceiptLine:
    description: str
    quantity: int
    unit_price: Money


@dataclass(frozen=True)
class ReceiptRequest:
    transaction_id: str
    total: Money
    lines: tuple[ReceiptLine, ...]
    customer_identification: str | None = None


@dataclass(frozen=True)
class ReceiptResult:
    accepted: bool
    receipt_key: str | None
    message: str


class AbstractReceiptService(ABC):
    """Interfaz esperada por el POS para emitir un comprobante."""

    @abstractmethod
    def issue(self, request: ReceiptRequest) -> ReceiptResult:
        raise NotImplementedError
