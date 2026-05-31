from decimal import Decimal

from pos_coffee_shop_kiosk.application.dtos.register_product_request import RegisterProductRequest
from pos_coffee_shop_kiosk.application.use_cases.inventory.register_product import RegisterProduct
from pos_coffee_shop_kiosk.application.use_cases.inventory.find_product import FindProduct
from pos_coffee_shop_kiosk.application.use_cases.inventory.list_products import ListProducts
from pos_coffee_shop_kiosk.application.use_cases.inventory.update_product import UpdateProduct
from pos_coffee_shop_kiosk.application.use_cases.inventory.remove_product import RemoveProduct
from pos_coffee_shop_kiosk.application.use_cases.inventory.find_products_by_category import FindProductsByCategory

from pos_coffee_shop_kiosk.infrastructure.repositories.json_product_repository import JsonProductRepository
from pos_coffee_shop_kiosk.infrastructure.repositories.json_product_category_repository import JsonProductCategoryRepository
from pos_coffee_shop_kiosk.infrastructure.repositories.json_tax_option_repository import JsonTaxOptionRepository


def print_product(product):
    print(f"Nombre: {product.name}")
    print(f"Descripción: {product.description}")
    print(f"Categoría: {product.category_name}")
    print(f"SKU: {product.sku}")
    print(f"Precio: ₡{product.price}")
    print(f"Stock: {product.stock}")
    print("-" * 30)

def product_exists(find_product, sku: str) -> bool:
    try:
        find_product.execute(sku)
        return True
    except ValueError:
        return False

def main():
    product_repository = JsonProductRepository()
    category_repository = JsonProductCategoryRepository()
    tax_option_repository = JsonTaxOptionRepository()

    register_product = RegisterProduct(
        product_repository,
        category_repository,
        tax_option_repository,
    )

    find_product = FindProduct(product_repository)
    list_products = ListProducts(product_repository)
    update_product = UpdateProduct(product_repository)
    remove_product = RemoveProduct(product_repository)
    find_products_by_category = FindProductsByCategory(product_repository)

    while True:
        print("\nDEMO INVENTARIO POS ")
        print("1. Registrar producto")
        print("2. Consultar producto por SKU")
        print("3. Listar productos")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Buscar productos por categoría")
        print("0. Salir")

        option = input("Seleccione una opción: ")
        
        try:
            if option == "1":
                name = input("Nombre: ")
                description = input("Descripción: ")
                category_name = input("Categoría: ")
                sub_category_name = input("Subcategoría: ")
                sku = input("SKU: ")
                price = Decimal(input("Precio: "))
                stock = Decimal(input("Stock: "))

                request = RegisterProductRequest(
                    name=name,
                    description=description,
                    category_name=category_name,
                    sub_category_name=sub_category_name,
                    sku=sku,
                    price=price,
                    stock=stock,
                    tax_options=[],
                )

                register_product.execute(request)
                print("\nProducto registrado correctamente.")

            elif option == "2":
                sku = input("Ingrese el SKU: ")
                if not product_exists(find_product, sku):
                    print("\nNo existe un producto con ese SKU.")
                    continue
                product = find_product.execute(sku)

                print("\nPRODUCTO ENCONTRADO ")
                print_product(product)

            elif option == "3":
                products = list_products.execute()

                print("\nLISTA DE PRODUCTOS ")

                if not products:
                    print("No hay productos registrados.")
                else:
                    for product in products:
                        print_product(product)

            elif option == "4":
                sku = input("SKU del producto a modificar: ")
                if not product_exists(find_product, sku):
                    print("\nNo existe un producto con ese SKU.")
                    continue

                new_price_input = input("Nuevo precio, deje vacío si no desea cambiarlo: ")
                stock_to_add_input = input("Stock a agregar, deje vacío si no desea agregar: ")
                stock_to_remove_input = input("Stock a remover, deje vacío si no desea remover: ")

                new_price = Decimal(new_price_input) if new_price_input else None
                stock_to_add = Decimal(stock_to_add_input) if stock_to_add_input else None
                stock_to_remove = Decimal(stock_to_remove_input) if stock_to_remove_input else None

                update_product.execute(
                    product_sku=sku,
                    new_price=new_price,
                    stock_to_add=stock_to_add,
                    stock_to_remove=stock_to_remove,
                )

                print("\nProducto actualizado correctamente.")

            elif option == "5":
                sku = input("SKU del producto a eliminar: ")
                if not product_exists(find_product, sku):
                    print("\nNo existe un producto con ese SKU.")
                    continue
                remove_product.execute(sku)

                print("\nProducto eliminado correctamente.")

            elif option == "6":
                category_name = input("Categoría: ")
                products = find_products_by_category.execute(category_name)

                print(f"\nPRODUCTOS EN CATEGORÍA: {category_name} ")

                if not products:
                    print("No hay productos en esta categoría.")
                else:
                    for product in products:
                        print_product(product)

            elif option == "0":
                print("Saliendo de la demo...")
                break

            else:
                print("Opción inválida.")
        except Exception as error:
            print(f"\nOcurrió un Error")
        


if __name__ == "__main__":
    main()