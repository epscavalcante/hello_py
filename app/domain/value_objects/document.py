import re
from dataclasses import dataclass

from app.domain.exceptions.invalid_document import (
    InvalidDocumentException,
)


@dataclass(frozen=True)
class Document:
    MAX_LENGTH = 11

    value: str

    def __post_init__(self) -> None:
        if not self._is_valid_cpf(self.value):
            raise InvalidDocumentException('Invalid CPF.')

    def _is_valid_cpf(self, cpf: str) -> bool:
        cpf = re.sub(r'\D', '', cpf)

        if len(cpf) != self.MAX_LENGTH or cpf == cpf[0] * self.MAX_LENGTH:
            return False

        for i in range(9, 11):
            value = sum(int(cpf[num]) * ((i + 1) - num) for num in range(0, i))
            digit = ((value * 10) % 11) % 10
            if digit != int(cpf[i]):
                return False

        return True

    def __str__(self) -> str:
        return self.value
