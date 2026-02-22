from abc import ABC, abstractmethod

from app.domain.entities.account import Account
from app.domain.value_objects.account_id import AccountId
from app.domain.value_objects.email import Email


class AccountRepository(ABC):
    @abstractmethod
    async def save(self, account: Account) -> None:
        pass

    @abstractmethod
    async def get_by_id(self, account_id: AccountId) -> Account | None:
        pass

    @abstractmethod
    async def get_by_email(self, email: Email) -> Account | None:
        pass
