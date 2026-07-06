from __future__ import annotations

from html import escape
from typing import Protocol

from pos_coffee_shop_kiosk.domain.interfaces.abstract_receipt_service import (
    AbstractReceiptService,
    ReceiptRequest,
    ReceiptResult,
)


class LegacyHaciendaApi(Protocol):
    """Forma de una API/SDK externo que el dominio no debe conocer."""

    def send_xml(self, api_token: str, xml_document: str) -> dict[str, object]:
        ...


class HaciendaReceiptAdapter(AbstractReceiptService):
    """Adapta la API externa de Hacienda a ``AbstractReceiptService``."""

    def __init__(self, external_api: LegacyHaciendaApi, api_token: str) -> None:
        self._external_api = external_api
        self._api_token = api_token

    def issue(self, request: ReceiptRequest) -> ReceiptResult:
        xml_document = self._to_xml(request)
        raw_response = self._external_api.send_xml(self._api_token, xml_document)

        status = str(raw_response.get("estado", "rechazado")).lower()
        accepted = status in {"aceptado", "accepted", "ok"}
        receipt_key_value = raw_response.get("clave")
        message_value = raw_response.get("mensaje", status)

        return ReceiptResult(
            accepted=accepted,
            receipt_key=str(receipt_key_value) if receipt_key_value else None,
            message=str(message_value),
        )

    @staticmethod
    def _to_xml(request: ReceiptRequest) -> str:
        customer = escape(request.customer_identification or "CONSUMIDOR_FINAL")
        lines = "".join(
            (
                "<Linea>"
                f"<Descripcion>{escape(line.description)}</Descripcion>"
                f"<Cantidad>{line.quantity}</Cantidad>"
                f"<PrecioUnitario>{line.unit_price.amount()}</PrecioUnitario>"
                "</Linea>"
            )
            for line in request.lines
        )
        return (
            "<Comprobante>"
            f"<Transaccion>{escape(request.transaction_id)}</Transaccion>"
            f"<Cliente>{customer}</Cliente>"
            f"<Moneda>{escape(request.total.currency().value)}</Moneda>"
            f"<Total>{request.total.amount()}</Total>"
            f"<Lineas>{lines}</Lineas>"
            "</Comprobante>"
        )
