from __future__ import annotations

from pos_coffee_shop_kiosk.domain.states.sale_state import SaleState


class SuccessSaleState(SaleState):
    def complete(self, sale) -> None:
        raise ValueError("La venta ya fue completada")

    def fail(self, sale) -> None:
        raise ValueError("No se puede fallar una venta completada")