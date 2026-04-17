from __future__ import annotations
from decimal import Decimal


class TaxOptionResponse:
    description: str
    percentage: Decimal

    def __init__(self, description: str, percentage: Decimal) -> None:
        self.description = description
        self.percentage = percentage