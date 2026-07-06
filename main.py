from pos_coffee_shop_kiosk.composition.create_use_cases import create_kiosk_use_cases
from pos_coffee_shop_kiosk.presentation.pos_kiosk_app import PosKioskApp


def select_branch() -> str:
    print("\nSeleccionar sucursal")
    print("1. San José")
    print("2. Alajuela")
    print("3. Cartago")

    option = input("Sucursal: ")

    if option == "1":
        return "san_jose"
    if option == "2":
        return "alajuela"
    if option == "3":
        return "cartago"

    print("Sucursal inválida. Se usará San José por defecto.")
    return "san_jose"


def main():
    branch = select_branch()
    kiosk_use_cases = create_kiosk_use_cases(branch)
    app = PosKioskApp(kiosk_use_cases, branch)
    app.run()


if __name__ == "__main__":
    main()