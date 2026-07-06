from __future__ import annotations
from abc import ABC, abstractmethod
from uuid import UUID
from datetime import datetime

from pos_coffee_shop_kiosk.domain.models.entities.sale import Sale
from pos_coffee_shop_kiosk.domain.models.shopping_cart import ShoppingCart
from pos_coffee_shop_kiosk.domain.enums.payment_method_type import PaymentMethodType
from pos_coffee_shop_kiosk.domain.models.value_objects.money import Money
from pos_coffee_shop_kiosk.domain.enums.sale_status import SaleStatus


class AbstractSaleFactory(ABC):
    @abstractmethod
    def create(
        self,
        sale_id: UUID,
        cart: ShoppingCart,
        payment_method: PaymentMethodType,
        amount_paid: Money,
        change: Money | None = None,
        status: SaleStatus = SaleStatus.PENDING,
        timestamp: datetime | None = None,
    ) -> Sale:
        pass