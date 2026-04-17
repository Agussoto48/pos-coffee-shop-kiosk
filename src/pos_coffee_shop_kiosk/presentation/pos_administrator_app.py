from pos_coffee_shop_kiosk.application.containers.administrator_app_use_cases import AdministratorAppUseCases


class PosAdministratorApp:
    def __init__(self, use_cases: AdministratorAppUseCases) -> None:
        self._use_cases = use_cases

    def run(self) -> None:
        pass
