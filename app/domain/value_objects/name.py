from dataclasses import dataclass

from app.domain.exceptions.invalid_name import InvalidNameException


@dataclass(frozen=True)
class Name:
    MIN_LENGTH = 2

    first_name: str
    last_name: str

    def __post_init__(self) -> None:
        first_name = self.first_name.strip()
        last_name = self.last_name.strip()

        if not first_name or not last_name:
            raise InvalidNameException('First and last name are required.')

        if (
            len(first_name) < self.MIN_LENGTH
            or len(last_name) < self.MIN_LENGTH
        ):
            raise InvalidNameException(
                f'Name parts must have at least {self.MIN_LENGTH} characters.'
            )

        object.__setattr__(self, 'first_name', first_name)
        object.__setattr__(self, 'last_name', last_name)

    def __str__(self) -> str:
        return self.first_name.strip() + ' ' + self.last_name.strip()
