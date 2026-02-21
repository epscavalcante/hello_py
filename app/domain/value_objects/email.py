import re
from dataclasses import dataclass

from app.domain.exceptions.invalid_email import InvalidEmailException


@dataclass(frozen=True)
class Email:
    value: str

    def __post_init__(self) -> None:
        normalized = self.value.strip().lower()
        if '@' not in normalized:
            raise InvalidEmailException('Invalid email format.')

        pattern = r'^[^@]+@[^@]+\.[^@]+$'
        if not re.match(pattern, normalized):
            raise InvalidEmailException('Invalid email format.')

        object.__setattr__(self, 'value', normalized)

    def __str__(self) -> str:
        return self.value
