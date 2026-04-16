from __future__ import annotations
from pos_coffee_shop_kiosk.domain.interfaces.abstract_summary_report_generator import AbstractSummaryReportGenerator


class TxtSummaryReportGenerator(AbstractSummaryReportGenerator):

    def generate(self) -> None:
        pass