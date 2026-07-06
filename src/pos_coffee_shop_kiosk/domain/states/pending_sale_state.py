from __future__ import annotations

from pos_coffee_shop_kiosk.domain.enums.sale_status import SaleStatus
from pos_coffee_shop_kiosk.domain.states.sale_state import SaleState


class PendingSaleState(SaleState):
    def complete(self, sale) -> None:
        sale._status = SaleStatus.SUCCESS
        sale._state = sale._success_state

    def fail(self, sale) -> None:
        sale._status = SaleStatus.FAILURE
        sale._state = sale._failure_state