class AdministratorAppUseCases:
    def __init__(
        self,
        product: ProductInventoryUseCases,
        category: ProductCategoryUseCases,
        pricing_options: PricingOptionsUseCases,
        reporting: ReportingUseCases,
    ) -> None:
        self.product = product
        self.category = category
        self.pricing_options = pricing_options
        self.reporting = reporting