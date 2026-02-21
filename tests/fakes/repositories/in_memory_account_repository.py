from app.domain.entities.account import Account
from app.domain.repositories.account import AccountRepository
from app.domain.value_objects.account_id import AccountId
from app.domain.value_objects.email import Email


class InMemoryAccountRepository(AccountRepository):
    def __init__(self):
        self.accounts = {}

    def save(self, account: Account) -> None:
        self.accounts[account.id] = account

    def get_by_id(self, account_id: AccountId) -> Account | None:
        return self.accounts.get(account_id)

    def get_by_email(self, email: Email) -> Account | None:
        return next(
            (a for a in self.accounts.values() if a.email == email), None
        )

    def exists(self, email: Email) -> bool:
        return any(a.email == email for a in self.accounts.values())
