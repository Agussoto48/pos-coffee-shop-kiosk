from __future__ import annotations
from pos_coffee_shop_kiosk.domain.observers.sale_observer import SaleObserver


class ReceiptSaleObserver(SaleObserver):
    def update(self, sale) -> None:
        print("Comprobante generado para la venta.")