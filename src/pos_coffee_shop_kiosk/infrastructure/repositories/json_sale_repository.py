from __future__ import annotations
from uuid import UUID
from pos_coffee_shop_kiosk.domain.interfaces.abstract_sale_repository import AbstractSaleRepository
from pos_coffee_shop_kiosk.domain.models.entities.sale import Sale


class JsonSaleRepository(AbstractSaleRepository):

    def add(self, sale: Sale) -> None:
        pass

    def remove(self, sale_id: UUID) -> None:
        pass

    def find_by_id(self, sale_id: UUID) -> Sale | None:
        pass

    def fetch_all_sales(self) -> list[Sale]:
        pass