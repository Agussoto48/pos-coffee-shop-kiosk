from __future__ import annotations


class TaxDescription:
    _text: str

    def __init__(self, description: str) -> None:
        self._text = description

    def _validate(self, description: str) -> None:
        pass

    def __eq__(self, other: object) -> bool:
        return isinstance(other, TaxDescription) and self._text == other._text

    def __hash__(self) -> int:
        return self._text.__hash__()

    def __str__(self) -> str:
        return self._text

    def text(self) -> str:
        return self._text