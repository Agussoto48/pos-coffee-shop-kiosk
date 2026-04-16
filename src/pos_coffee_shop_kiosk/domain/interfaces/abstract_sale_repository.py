from __future__ import annotations
from abc import ABC, abstractmethod
from uuid import UUID
from pos_coffee_shop_kiosk.domain.models.entities.sale import Sale


class AbstractSaleRepository(ABC):

    @abstractmethod
    def add(self, sale: Sale) -> None:
        pass

    @abstractmethod
    def remove(self, sale_id: UUID) -> None:
        pass

    @abstractmethod
    def find_by_id(self, sale_id: UUID) -> Sale | None:
        pass

    @abstractmethod
    def fetch_all_sales(self) -> list[Sale]:
        pass