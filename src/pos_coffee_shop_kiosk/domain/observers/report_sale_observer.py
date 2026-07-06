from __future__ import annotations
from pos_coffee_shop_kiosk.domain.observers.sale_observer import SaleObserver


class ReportSaleObserver(SaleObserver):
    def update(self, sale) -> None:
        print("Reporte de ventas actualizado.")