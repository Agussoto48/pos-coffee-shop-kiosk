from __future__ import annotations
from decimal import Decimal
from datetime import datetime


class ClientPaymentDetails:
    amount_tendered: Decimal | None
    card_holder: str | None
    card_number: str | None
    expiration_date: datetime | None
    security_code: Decimal | None

    def __init__(
        self,
        amount_tendered: Decimal | None = None,
        card_holder: str | None = None,
        card_number: str | None = None,
        expiration_date: datetime | None = None,
        security_code: Decimal | None = None,
    ) -> None:
        self.amount_tendered = amount_tendered
        self.card_holder = card_holder
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.security_code = security_code