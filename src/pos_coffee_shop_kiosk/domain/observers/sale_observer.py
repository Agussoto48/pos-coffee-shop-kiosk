from __future__ import annotations
from abc import ABC, abstractmethod


class SaleObserver(ABC):
    @abstractmethod
    def update(self, sale) -> None:
        pass