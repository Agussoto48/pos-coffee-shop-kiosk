from __future__ import annotations
from abc import ABC, abstractmethod
from pos_coffee_shop_kiosk.domain.models.dtos.tax_option import TaxOption
from pos_coffee_shop_kiosk.domain.models.value_objects.TaxDescription import TaxDescription


class AbstractTaxOptionRepository(ABC):

    @abstractmethod
    def add(self, tax_option: TaxOption) -> None:
        pass

    @abstractmethod
    def remove(self, tax_option: TaxOption) -> None:
        pass

    @abstractmethod
    def find_by_description(self, description: TaxDescription) -> TaxOption | None:
        pass

    @abstractmethod
    def fetch_all_tax_options(self) -> list[TaxOption]:
        pass