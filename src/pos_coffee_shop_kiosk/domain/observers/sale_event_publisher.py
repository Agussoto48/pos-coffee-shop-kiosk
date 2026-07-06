from __future__ import annotations
from pos_coffee_shop_kiosk.domain.observers.sale_observer import SaleObserver


class SaleEventPublisher:
    def __init__(self) -> None:
        self._observers: list[SaleObserver] = []

    def subscribe(self, observer: SaleObserver) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: SaleObserver) -> None:
        self._observers.remove(observer)

    def notify(self, sale) -> None:
        for observer in self._observers:
            observer.update(sale)