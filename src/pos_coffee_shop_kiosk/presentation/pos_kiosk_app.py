from __future__ import annotations
from decimal import Decimal
from pos_coffee_shop_kiosk.application.containers.kiosk_app_use_cases import KioskAppUseCases
from pos_coffee_shop_kiosk.application.dtos.client_payment_details import ClientPaymentDetails
from pos_coffee_shop_kiosk.domain.enums.payment_method_type import PaymentMethodType
from datetime import datetime


class PosKioskApp:
    def __init__(self, use_cases: KioskAppUseCases, branch: str) -> None:
        self._use_cases = use_cases
        self._branch = branch

    def run(self) -> None:
        while True:
            print(f"\nPOS KIOSK | Sucursal: {self._branch} ")
            print("1. Ver lista de productos")
            print("2. Agregar producto al carrito")
            print("3. Remover producto del carrito")
            print("4. Ver carrito")
            print("5. Vaciar carrito")
            print("6. Procesar checkout")
            print("0. Salir")

            option = input("Seleccione una opción: ")

            try:
                if option == "1":
                    products = self._use_cases.browse_menu.execute()

                    print("\nPRODUCTOS DISPONIBLES ")

                    if not products:
                        print("No hay productos registrados.")
                    else:
                        for product in products:
                            print(f"Nombre: {product.name}")
                            print(f"SKU: {product.sku}")
                            print(f"Categoría: {product.category_name}")
                            print(f"Precio: {product.price}")
                            print(f"Stock: {product.stock}")
                            print("-" * 30)
                if option == "2":
                    sku = input("SKU del producto: ")
                    quantity = int(input("Cantidad: "))
                    self._use_cases.shopping_cart.add_cart_item.execute(sku, quantity)
                    print("Producto agregado al carrito.")

                elif option == "3":
                    sku = input("SKU del producto: ")
                    quantity = int(input("Cantidad a remover: "))
                    self._use_cases.shopping_cart.remove_cart_item.execute(sku, quantity)
                    print("Producto removido del carrito.")

                elif option == "4":
                    summary = self._use_cases.shopping_cart.fetch_cart_summary.execute()
                    print("\nCARRITO ")

                    if summary.is_empty:
                        print("El carrito está vacío.")
                    else:
                        for item in summary.items:
                            print(f"Producto: {item.product_name}")
                            print(f"SKU: {item.sku}")
                            print(f"Cantidad: {item.quantity}")
                            print(f"Precio unitario: {item.unit_price}")
                            print(f"Subtotal: {item.subtotal}")
                            print("-" * 30)

                        print("Total:", summary.total)

                elif option == "5":
                    self._use_cases.shopping_cart.clear_cart.execute()
                    print("Carrito vaciado.")

                elif option == "6":
                    print("\nMÉTODO DE PAGO")
                    print("1. Efectivo")
                    print("2. Tarjeta")
                    print("3. Tap")

                    payment_option = input("Seleccione método de pago: ")

                    if payment_option == "1":
                        amount = Decimal(input("Monto entregado en efectivo: "))

                        payment_method_type = PaymentMethodType.CASH
                        client_details = ClientPaymentDetails(
                            amount_tendered=amount,
                        )

                    elif payment_option == "2":
                        card_number = input("Número de tarjeta: ")
                        card_holder = input("Nombre del titular: ")
                        expiration_input = input("Fecha de expiración MM/YY: ")
                        security_code = input("Código de seguridad: ")

                        month, year = expiration_input.split("/")
                        expiration_date = datetime(
                            year=2000 + int(year),
                            month=int(month),
                            day=1,
                        )

                        payment_method_type = PaymentMethodType.CARD
                        client_details = ClientPaymentDetails(
                            card_number=card_number,
                            card_holder=card_holder,
                            expiration_date=expiration_date,
                            security_code=security_code,
                        )

                    elif payment_option == "3":
                        card_number = input("Número de tarjeta: ")
                        card_holder = input("Nombre del titular: ")

                        payment_method_type = PaymentMethodType.TAP_CARD
                        client_details = ClientPaymentDetails(
                            card_number=card_number,
                            card_holder=card_holder,
                        )

                    else:
                        print("Método de pago inválido.")
                        continue

                    payment_method = self._use_cases.checkout.create_payment_method.execute(
                        payment_method_type,
                        client_details,
                    )

                    sale = self._use_cases.checkout.process_checkout.execute(
                        payment_method_type,
                        payment_method,
                    )

                    print("\nVENTA COMPLETADA")
                    print("ID:", sale.sale_id())
                    print("Estado:", sale.status().value)

                elif option == "0":
                    print("Saliendo del kiosco...")
                    break

                else:
                    print("Opción inválida.")

            except Exception as error:
                print(f"Error: {error}")