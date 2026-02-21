from sqlalchemy.orm import Session

from app.domain.entities.account import Account
from app.domain.repositories.account import AccountRepository
from app.domain.value_objects.account_id import AccountId
from app.domain.value_objects.email import Email
from app.domain.value_objects.name import Name
from app.infraestructure.models.account import AccountModel


class SqlAlchemyAccountRepository(AccountRepository):
    def __init__(self, session: Session):
        self._session = session

    def save(self, account: Account) -> None:
        model = AccountModel(
            account_id=str(account.id),
            first_name=account.name.first_name,
            last_name=account.name.last_name,
            email=str(account.email),
            is_active=account.is_active,
        )

        self._session.merge(model)
        self._session.commit()

    def get_by_id(self, account_id: AccountId) -> Account | None:
        model = self._session.get(AccountModel, str(account_id))

        if not model:
            return None

        return Account(
            account_id=AccountId.from_str(model.account_id),
            name=Name(model.first_name, model.last_name),
            email=Email(model.email),
            # is_active=model.is_active,
        )


def get_by_email(self, email: Email) -> Account | None:
    model = (
        self._session
        .query(AccountModel)
        .filter(AccountModel.email == str(email))
        .first()
    )

    if not model:
        return None

    return Account(
        account_id=AccountId.from_str(model.account_id),
        name=Name(model.first_name, model.last_name),
        email=Email(model.email),
        # is_active=model.is_active,
    )
