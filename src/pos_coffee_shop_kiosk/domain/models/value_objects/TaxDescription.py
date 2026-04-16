from __future__ import annotations


class TaxDescription:
    _text: str

    def __init__(self, description: str) -> None:
        self._text = description

    def _validate(self, description: str) -> None:
        pass

    def __eq__(self, other: TaxDescription) -> bool:
        pass

    def __hash__(self) -> int:
        pass

    def __str__(self) -> str:
        pass

    def text(self) -> str:
        pass