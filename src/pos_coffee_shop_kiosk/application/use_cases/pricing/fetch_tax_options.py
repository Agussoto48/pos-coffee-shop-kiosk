from __future__ import annotations

class FetchTaxOptions:
    def __init__(
        self,
        tax_option_repository: AbstractTaxOptionRepository,
    ) -> None:
        self.tax_option_repository = tax_option_repository

    def execute(self) -> list[TaxOptionResponse]:
        pass
