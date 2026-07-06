from __future__ import annotations
from uuid import UUID
from pos_coffee_shop_kiosk.domain.interfaces.abstract_sale_repository import AbstractSaleRepository
from pos_coffee_shop_kiosk.domain.models.entities.sale import Sale


class JsonSaleRepository(AbstractSaleRepository):
    def __init__(self) -> None:
        self._sales: dict[UUID, Sale] = {}

    def add(self, sale: Sale) -> None:
        self._sales[sale.sale_id()] = sale

    def remove(self, sale_id: UUID) -> None:
        self._sales.pop(sale_id, None)

    def find_by_id(self, sale_id: UUID) -> Sale | None:
        return self._sales.get(sale_id)

    def fetch_all_sales(self) -> list[Sale]:
        return list(self._sales.values())