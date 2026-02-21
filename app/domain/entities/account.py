from app.domain.value_objects.account_id import AccountId
from app.domain.value_objects.email import Email
from app.domain.value_objects.name import Name


class Account:
    def __init__(self, account_id: AccountId, name: Name, email: Email):
        self._account_id = account_id
        self._name = name
        self._email = email

    @classmethod
    def create(cls, name: Name, email: Email):
        account = cls(AccountId.new(), name, email)
        return account

    @property
    def id(self):
        return self._account_id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    def get_email(self) -> str:
        return self._email.value

    def get_first_name(self) -> str:
        return self._name.first_name

    def get_last_name(self) -> str:
        return self._name.last_name

    def get_full_name(self):
        return str(self._name)
