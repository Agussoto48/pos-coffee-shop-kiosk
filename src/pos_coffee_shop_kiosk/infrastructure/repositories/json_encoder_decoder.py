from pos_coffee_shop_kiosk.domain.models.entities.product import Product
from pos_coffee_shop_kiosk.domain.models.value_objects.sku import Sku
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.models.value_objects.product_category import ProductCategory
from pos_coffee_shop_kiosk.domain.models.value_objects.product_name import ProductName
from pos_coffee_shop_kiosk.domain.models.value_objects.tax_option import TaxOption

REGISTRY = {
    "Sku": Sku,
    "Money": Money,
    "Product": Product,
    "TaxOption": TaxOption,
    "ProductCategory": ProductCategory,
    "ProductName": ProductName,
}

def decode(dct: dict) -> object:
    type_name = dct.get("__type__")
    if type_name in REGISTRY:
        return REGISTRY[type_name].from_dict(dct)
    return dct

def encode(obj: object) -> object:
    if hasattr(obj, "to_dict"):
        return obj.to_dict() # type: ignore
    raise TypeError(f"Cannot serialize {type(obj)}")