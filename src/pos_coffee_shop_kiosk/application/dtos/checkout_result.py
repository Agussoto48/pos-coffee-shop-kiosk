from __future__ import annotations

from dataclasses import dataclass

from pos_coffee_shop_kiosk.domain.interfaces.abstract_receipt_service import ReceiptResult
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.pricing.pricing_component import PriceAdjustment


@dataclass(frozen=True)
class CheckoutPreview:
    total: Money
    breakdown: tuple[PriceAdjustment, ...]


@dataclass(frozen=True)
class CheckoutResult:
    completed: bool
    total: Money
    transaction_id: str | None
    message: str
    receipt: ReceiptResult | None
