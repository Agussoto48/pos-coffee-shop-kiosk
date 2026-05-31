from decimal import Decimal

from pos_coffee_shop_kiosk.application.dtos.register_product_request import RegisterProductRequest
from pos_coffee_shop_kiosk.application.use_cases.inventory.register_product import RegisterProduct
from pos_coffee_shop_kiosk.application.use_cases.inventory.find_product import FindProduct
from pos_coffee_shop_kiosk.infrastructure.repositories.json_product_repository import JsonProductRepository



#Clases para ver si agregar/encontrar funcionan correctamente
#Luego se cambian para que funcione con las clases ya definidas
class FakeCategoryRepository:
    def add(self, category):
        pass

    def remove(self, category):
        pass

    def find_by_name(self, name):
        return None

    def fetch_all_categories(self):
        return []


class FakeTaxOptionRepository:
    def add(self, tax_option):
        pass

    def remove(self, tax_option):
        pass

    def find_by_description(self, description):
        return None

    def fetch_all_tax_options(self):
        return []


def main():
    product_repository = JsonProductRepository()
    category_repository = FakeCategoryRepository()
    tax_option_repository = FakeTaxOptionRepository()

    register_product = RegisterProduct(
        product_repository,
        category_repository,
        tax_option_repository,
    )

    find_product = FindProduct(product_repository)

    request = RegisterProductRequest(
        name="Café Latte",
        description="Café con leche",
        category_name="Bebidas",
        sub_category_name="Café",
        sku="LATTE-001",
        price=Decimal("2500"),
        stock=Decimal("10"),
        tax_options=[],
    )

    register_product.execute(request)

    print("Producto registrado correctamente.")
    print()

    product = find_product.execute("LATTE-001")

    print("Producto encontrado:")
    print("Nombre:", product.name)
    print("Descripción:", product.description)
    print("Categoría:", product.category_name)
    print("SKU:", product.sku)
    print("Precio:", product.price)
    print("Stock:", product.stock)


if __name__ == "__main__":
    main()