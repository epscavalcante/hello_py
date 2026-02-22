import pytest

from app.application.use_cases.signup.signup_input import SignupInput
from app.application.use_cases.signup.signup_output import SignupOutput
from app.domain.entities.account import Account
from app.domain.exceptions.email_already_exists import (
    EmailAlreadyExistsException,
)
from app.domain.repositories.account import AccountRepository
from app.domain.value_objects.email import Email
from app.domain.value_objects.name import Name

# from app.application.ports import UnitOfWork


class Signup:
    def __init__(self, account_repository: AccountRepository):
        self._account_repository = account_repository

    async def execute(self, data: SignupInput) -> SignupOutput:
        email = Email(data.email)
        account_exists = await self._account_repository.get_by_email(email)

        if account_exists:
            raise EmailAlreadyExistsException('Email already exists')

        name = Name(data.first_name, data.last_name)
        account = Account.create(name, email)

        return SignupOutput(account_id=str(account.id))
