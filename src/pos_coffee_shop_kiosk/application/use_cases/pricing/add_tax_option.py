from __future__ import annotations

from decimal import Decimal


class AddTaxOption:
    def __init__(
        self,
        tax_option_repository: AbstractTaxOptionRepository,
    ) -> None:
        self.tax_option_repository = tax_option_repository

    def execute(self, tax_description: str, percentage_value: Decimal) -> None:
        pass
