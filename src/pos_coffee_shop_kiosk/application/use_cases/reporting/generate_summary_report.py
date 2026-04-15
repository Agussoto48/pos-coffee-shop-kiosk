from __future__ import annotations

class GenerateSummaryReport:
    def __init__(
        self,
        sale_repository: AbstractSaleRepository,
    ) -> None:
        self.sale_repository = sale_repository

    def execute(self) -> None:
        pass
