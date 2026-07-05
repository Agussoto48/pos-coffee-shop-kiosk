from __future__ import annotations
from pos_coffee_shop_kiosk.domain.observers.sale_observer import SaleObserver


class InventorySaleObserver(SaleObserver):
    def update(self, sale) -> None:
        print("Inventario actualizado después de la venta.")