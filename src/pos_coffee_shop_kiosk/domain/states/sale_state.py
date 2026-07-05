from __future__ import annotations
from abc import ABC, abstractmethod


class SaleState(ABC):
    @abstractmethod
    def complete(self, sale) -> None:
        pass

    @abstractmethod
    def fail(self, sale) -> None:
        pass