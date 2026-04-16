from __future__ import annotations
from decimal import Decimal
from pos_coffee_shop_kiosk.domain.enums.currency import Currency


class Money:
    _amount: Decimal
    _currency: Currency

    def __init__(self, amount: Decimal, currency: Currency) -> None:
        self._amount = amount
        self._currency = currency

    def _validate(self, amount: Decimal, currency: Currency) -> None:
        pass

    def __eq__(self, other: Money) -> bool:
        pass

    def __hash__(self) -> int:
        pass

    def __str__(self) -> str:
        pass

    def add(self, other: Money) -> Money:
        pass

    def subtract(self, other: Money) -> Money:
        pass

    def amount(self) -> Decimal:
        pass

    def currency(self) -> Currency:
        pass