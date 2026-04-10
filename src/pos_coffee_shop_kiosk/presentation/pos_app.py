from pos_coffee_shop_kiosk.presentation.pos_administrator_app import PosAdministratorApp
from pos_coffee_shop_kiosk.presentation.pos_kiosk_app import PosKioskApp


class PosApp:
    def __init__(
        self, pos_administrator_app: PosAdministratorApp, pos_kiosk_app: PosKioskApp
    ):
        self._pos_administrator_app = pos_administrator_app
        self._pos_kiosk_app = pos_kiosk_app

    def run(self) -> None:
        pass
