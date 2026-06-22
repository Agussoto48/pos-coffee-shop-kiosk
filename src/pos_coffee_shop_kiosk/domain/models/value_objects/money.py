from __future__ import annotations
from decimal import Decimal
from pos_coffee_shop_kiosk.domain.enums.currency import Currency


class Money:
    _amount: Decimal
    _currency: Currency

    def __init__(self, amount: Decimal, currency: Currency) -> None:
        self._validate(amount, currency)
        self._amount = amount
        self._currency = currency

    def _validate(self, amount: Decimal, currency: Currency) -> None:
        if amount < 0:
            raise ValueError("El monto no puede ser negativo")

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Money)
            and self._amount == other._amount
            and self._currency == other._currency
        )

    def __hash__(self) -> int:
        return hash((self._amount, self._currency))

    def __str__(self) -> str:
        return f"{self._currency.value} {self._amount}"

    def add(self, other: Money) -> Money:
        if self._currency != other._currency:
            raise ValueError("No se pueden sumar monedas diferentes")
        return Money(self._amount + other._amount, self._currency)

    def subtract(self, other: Money) -> Money:
        if self._currency != other._currency:
            raise ValueError("No se pueden restar monedas diferentes")
        return Money(self._amount - other._amount, self._currency)

    def amount(self) -> Decimal:
         return self._amount

    def currency(self) -> Currency:
        return self._currency
    
    def to_dict(self):
        return {
            "__type__": "Money",
            "amount": str(self._amount),
            "currency": self._currency.value
        }

    @classmethod
    def from_dict(cls, d) -> Money:
        return cls(Decimal(str(d["amount"])), Currency(d["currency"]))
