from __future__ import annotations

from pos_coffee_shop_kiosk.domain.states.sale_state import SaleState


class FailureSaleState(SaleState):
    def complete(self, sale) -> None:
        raise ValueError("No se puede completar una venta fallida")

    def fail(self, sale) -> None:
        raise ValueError("La venta ya está fallida")