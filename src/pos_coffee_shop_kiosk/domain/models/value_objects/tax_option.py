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

    def __eq__(self, other: object) -> bool:
        if isinstance(other, TaxOption):
            return self._percentage == other._percentage\
                    and self._description == other._description
        return False

    def __hash__(self) -> int:
        return self._percentage.__hash__()

    def __str__(self) -> str:
        return f"TaxOption: {self._description}, {self._percentage}%"

    def description(self) -> TaxDescription:
        return self._description

    def percentage(self) -> Percentage:
        return self._percentage

    def to_dict(self) -> dict[str, str]:        
        return {
            "__type__": "TaxOption",
            "description": self._description.text(),
            "percentage": str(self._percentage.value())
        }

    @classmethod
    def from_dict(cls, d: dict[str, str]) -> TaxOption:
        return cls(d["description"], Decimal(d["percentage"]))
