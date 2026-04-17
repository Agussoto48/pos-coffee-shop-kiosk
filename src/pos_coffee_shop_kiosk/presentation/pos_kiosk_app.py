from pos_coffee_shop_kiosk.application.containers.kiosk_app_use_cases import KioskAppUseCases


class PosKioskApp:
    def __init__(self, use_cases: KioskAppUseCases) -> None:
        self._use_cases = use_cases

    def run(self) -> None:
        pass
