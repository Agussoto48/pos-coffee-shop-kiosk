from __future__ import annotations
from decimal import Decimal
from pos_coffee_shop_kiosk.domain.models.value_objects.tax_description import TaxDescription
from pos_coffee_shop_kiosk.domain.models.value_objects.percentage import Percentage


class TaxOption:
    _description: TaxDescription
    _percentage: Percentage

    def __init__(self, description: str, percentage: Decimal) -> None:
        self._description = TaxDescription(description)
        self._percentage = Percentage(percentage)

    def _validate(self, description: str, percentage: Decimal) -> None:
        pass

    def __eq__(self, other: TaxOption) -> bool:
        pass

    def __hash__(self) -> int:
        pass

    def __str__(self) -> str:
        pass

    def description(self) -> TaxDescription:
        pass

    def percentage(self) -> Percentage:
        pass