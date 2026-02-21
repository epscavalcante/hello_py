from uuid import uuid4


class AccountId:
    def __init__(self, value: str):
        self._value = value

    @classmethod
    def new(cls):
        return cls(str(uuid4()))

    @classmethod
    def from_str(cls, value: str):
        return cls(value)

    def __str__(self):
        return self._value

    def __eq__(self, other):
        return isinstance(other, AccountId) and self._value == other._value

    def __hash__(self):
        return hash(self._value)
