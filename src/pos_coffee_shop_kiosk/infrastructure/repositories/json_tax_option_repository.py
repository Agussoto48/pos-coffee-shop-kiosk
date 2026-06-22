from __future__ import annotations
import json
from pos_coffee_shop_kiosk.infrastructure.repositories import json_encoder_decoder
from pos_coffee_shop_kiosk.domain.interfaces.abstract_tax_option_repository import AbstractTaxOptionRepository
from pos_coffee_shop_kiosk.domain.models.value_objects.tax_option import TaxOption
from pos_coffee_shop_kiosk.domain.models.value_objects.tax_description import TaxDescription


class JsonTaxOptionRepository(AbstractTaxOptionRepository):
    __FILE_PATH: str = "tax_options.json"

    def __init__(self) -> None:
        try:
            with open(JsonTaxOptionRepository.__FILE_PATH) as f:
                taxes: list[TaxOption] = \
                    json.load(f, object_hook=json_encoder_decoder.decode)
                self._products = {t.description() : t for t in taxes}
        except FileNotFoundError:
            with open(JsonTaxOptionRepository.__FILE_PATH, "w") as f:
                json.dump([], f)
            self._tax_options: dict[TaxDescription, TaxOption] = {}

    def _save(self) -> None:
        with open(JsonTaxOptionRepository.__FILE_PATH, "w") as f:
            json.dump(list[self._tax_options.values()], f,\
                      default=json_encoder_decoder.encode)

    def add(self, tax_option: TaxOption) -> None:
        self._tax_options[tax_option.description()] = tax_option
        self._save()

    def remove(self, tax_option: TaxOption) -> None:
        self._tax_options.pop(tax_option.description(), None)
        self._save()

    def find_by_description(self, description: TaxDescription) -> TaxOption | None:
        return self._tax_options.get(description)

    def fetch_all_tax_options(self) -> list[TaxOption]:
        return list(self._tax_options.values())