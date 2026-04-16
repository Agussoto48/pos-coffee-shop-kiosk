from __future__ import annotations
from abc import ABC, abstractmethod
from pos_coffee_shop_kiosk.domain.interfaces.abstract_sale_repository import AbstractSaleRepository


class AbstractSummaryReportGenerator(ABC):

    def __init__(self, sale_repository: AbstractSaleRepository) -> None:
        self._sale_repository = sale_repository

    @abstractmethod
    def generate(self) -> None:
        pass