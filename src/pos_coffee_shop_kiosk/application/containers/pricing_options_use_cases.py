from __future__ import annotations

class PricingOptionsUseCases:
    def __init__(
        self,
        add_tax_option: AddTaxOption,
        remove_tax_option: RemoveTaxOption,
        fetch_tax_options: FetchTaxOptions,
    ) -> None:
        self.add_tax_option = add_tax_option
        self.remove_tax_option = remove_tax_option
        self.fetch_tax_options = fetch_tax_options
