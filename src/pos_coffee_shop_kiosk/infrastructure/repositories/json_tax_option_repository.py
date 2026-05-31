from __future__ import annotations
from pos_coffee_shop_kiosk.domain.interfaces.abstract_tax_option_repository import AbstractTaxOptionRepository
from pos_coffee_shop_kiosk.domain.models.value_objects.tax_option import TaxOption
from pos_coffee_shop_kiosk.domain.models.value_objects.tax_description import TaxDescription


class JsonTaxOptionRepository(AbstractTaxOptionRepository):

    def __init__(self) -> None:
        self._tax_options: dict[TaxDescription, TaxOption] = {}

    def add(self, tax_option: TaxOption) -> None:
        self._tax_options[tax_option.description()] = tax_option

    def remove(self, tax_option: TaxOption) -> None:
        self._tax_options.pop(tax_option.description(), None)

    def find_by_description(self, description: TaxDescription) -> TaxOption | None:
        return self._tax_options.get(description)

    def fetch_all_tax_options(self) -> list[TaxOption]:
        return list(self._tax_options.values())