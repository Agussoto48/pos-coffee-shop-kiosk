from __future__ import annotations

from decimal import Decimal

from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.pricing.pricing_component import (
    PriceAdjustment,
    PricingComponent,
    PricingDecorator,
)


def _validate_percentage(value: Decimal) -> None:
    if value < Decimal("0") or value > Decimal("100"):
        raise ValueError("El porcentaje debe estar entre 0 y 100")


def _percentage_of(base: Money, percentage: Decimal) -> Money:
    amount = base.amount() * percentage / Decimal("100")
    return Money(amount, base.currency())


class TaxDecorator(PricingDecorator):
    """Agrega un impuesto porcentual al resultado del componente envuelto."""

    def __init__(
        self,
        wrapped: PricingComponent,
        percentage: Decimal,
        description: str = "Impuesto",
    ) -> None:
        super().__init__(wrapped)
        _validate_percentage(percentage)
        self._percentage = percentage
        self._description = description

    def calculate_total(self) -> Money:
        base = self._wrapped.calculate_total()
        return base.add(_percentage_of(base, self._percentage))

    def breakdown(self) -> list[PriceAdjustment]:
        lines = super().breakdown()
        base = self._wrapped.calculate_total()
        tax = _percentage_of(base, self._percentage)
        lines.append(
            PriceAdjustment(
                f"{self._description} ({self._percentage}%)",
                tax,
                "charge",
            )
        )
        return lines


class PercentageDiscountDecorator(PricingDecorator):
    """Aplica un descuento porcentual al total calculado hasta ese punto."""

    def __init__(
        self,
        wrapped: PricingComponent,
        percentage: Decimal,
        description: str = "Descuento",
    ) -> None:
        super().__init__(wrapped)
        _validate_percentage(percentage)
        self._percentage = percentage
        self._description = description

    def calculate_total(self) -> Money:
        base = self._wrapped.calculate_total()
        discount = _percentage_of(base, self._percentage)
        return base.subtract(discount)

    def breakdown(self) -> list[PriceAdjustment]:
        lines = super().breakdown()
        base = self._wrapped.calculate_total()
        discount = _percentage_of(base, self._percentage)
        lines.append(
            PriceAdjustment(
                f"{self._description} ({self._percentage}%)",
                discount,
                "discount",
            )
        )
        return lines


class ThresholdPromotionDecorator(PricingDecorator):
    """Resta un monto fijo cuando el total alcanza un mínimo configurado."""

    def __init__(
        self,
        wrapped: PricingComponent,
        minimum_purchase: Money,
        discount: Money,
        description: str = "Promoción por compra mínima",
    ) -> None:
        super().__init__(wrapped)
        if minimum_purchase.currency() != discount.currency():
            raise ValueError("La compra mínima y el descuento deben usar la misma moneda")
        self._minimum_purchase = minimum_purchase
        self._discount = discount
        self._description = description

    def _effective_discount(self, base: Money) -> Money:
        if base.currency() != self._minimum_purchase.currency():
            raise ValueError("La promoción no corresponde a la moneda del carrito")
        if base.amount() < self._minimum_purchase.amount():
            return Money(Decimal("0"), base.currency())
        amount = min(base.amount(), self._discount.amount())
        return Money(amount, base.currency())

    def calculate_total(self) -> Money:
        base = self._wrapped.calculate_total()
        return base.subtract(self._effective_discount(base))

    def breakdown(self) -> list[PriceAdjustment]:
        lines = super().breakdown()
        base = self._wrapped.calculate_total()
        discount = self._effective_discount(base)
        if discount.amount() > 0:
            lines.append(PriceAdjustment(self._description, discount, "discount"))
        return lines
