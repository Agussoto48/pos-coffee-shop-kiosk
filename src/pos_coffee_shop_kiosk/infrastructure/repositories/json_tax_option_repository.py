from __future__ import annotations
from pos_coffee_shop_kiosk.domain.interfaces.abstract_tax_option_repository import AbstractTaxOptionRepository
from pos_coffee_shop_kiosk.domain.models.dtos.tax_option import TaxOption
from pos_coffee_shop_kiosk.domain.models.value_objects.TaxDescription import TaxDescription


class JsonTaxOptionRepository(AbstractTaxOptionRepository):

    def add(self, tax_option: TaxOption) -> None:
        pass

    def remove(self, tax_option: TaxOption) -> None:
        pass

    def find_by_description(self, description: TaxDescription) -> TaxOption | None:
        pass

    def fetch_all_tax_options(self) -> list[TaxOption]:
        pass