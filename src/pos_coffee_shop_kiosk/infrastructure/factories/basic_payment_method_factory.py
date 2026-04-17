from __future__ import annotations
from pos_coffee_shop_kiosk.domain.factories.abstract_payment_method_factory import AbstractPaymentMethodFactory
from pos_coffee_shop_kiosk.domain.factories.abstract_payment_factory import AbstractPaymentFactory
from pos_coffee_shop_kiosk.domain.interfaces.abstract_payment_method import AbstractPaymentMethod
from pos_coffee_shop_kiosk.domain.enums.payment_method_type import PaymentMethodType
from pos_coffee_shop_kiosk.application.dtos.client_payment_details import ClientPaymentDetails
from pos_coffee_shop_kiosk.infrastructure.factories.cash_payment_factory import CashPaymentFactory
from pos_coffee_shop_kiosk.infrastructure.factories.tap_card_payment_factory import TapCardPaymentFactory
from pos_coffee_shop_kiosk.infrastructure.factories.card_payment_factory import CardPaymentFactory


class BasicPaymentMethodFactory(AbstractPaymentMethodFactory):

    registry: dict[PaymentMethodType, AbstractPaymentFactory] = {
        PaymentMethodType.CASH: CashPaymentFactory(),
        PaymentMethodType.TAP_CARD: TapCardPaymentFactory(),
        PaymentMethodType.CARD: CardPaymentFactory(),
    }

    def create(
        self,
        methodType: PaymentMethodType,
        clientDetails: ClientPaymentDetails
    ) -> AbstractPaymentMethod:
        pass