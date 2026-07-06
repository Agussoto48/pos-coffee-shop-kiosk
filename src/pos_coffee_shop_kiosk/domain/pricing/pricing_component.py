from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal

from pos_coffee_shop_kiosk.domain.models.shopping_cart import ShoppingCart
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money


AdjustmentKind = Literal["base", "charge", "discount"]


@dataclass(frozen=True)
class PriceAdjustment:
    """Línea explicativa del cálculo final.

    El monto siempre es positivo. ``kind`` indica si la línea corresponde al
    subtotal, a un cargo o a una rebaja.
    """

    description: str
    amount: Money
    kind: AdjustmentKind


class PricingComponent(ABC):
    """Componente común de la cadena de cálculo de precios."""

    @abstractmethod
    def calculate_total(self) -> Money:
        """Devuelve el total producido por este componente."""
        raise NotImplementedError

    @abstractmethod
    def breakdown(self) -> list[PriceAdjustment]:
        """Devuelve el detalle acumulado de ajustes aplicados."""
        raise NotImplementedError


class CartSubtotal(PricingComponent):
    """Componente concreto: obtiene el subtotal original del carrito."""

    def __init__(self, shopping_cart: ShoppingCart) -> None:
        self._shopping_cart = shopping_cart

    def calculate_total(self) -> Money:
        return self._shopping_cart.get_total()

    def breakdown(self) -> list[PriceAdjustment]:
        subtotal = self.calculate_total()
        return [PriceAdjustment("Subtotal del carrito", subtotal, "base")]


class PricingDecorator(PricingComponent, ABC):
    """Decorador base que mantiene una referencia a otro componente."""

    def __init__(self, wrapped: PricingComponent) -> None:
        self._wrapped = wrapped

    def breakdown(self) -> list[PriceAdjustment]:
        return list(self._wrapped.breakdown())
