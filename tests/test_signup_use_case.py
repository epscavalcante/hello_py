import pytest

from app.application.use_cases.signup.signup import Signup
from app.application.use_cases.signup.signup_input import SignupInput
from app.application.use_cases.signup.signup_output import SignupOutput
from app.domain.entities.account import Account
from app.domain.exceptions.email_already_exists import (
    EmailAlreadyExistsException,
)
from app.domain.value_objects.email import Email
from app.domain.value_objects.name import Name
from tests.fakes.repositories.in_memory_account_repository import (
    InMemoryAccountRepository,
)


class TestSignupUseCase:
    def test_should_create_an_account(self):  # noqa: PLR6301
        account_repository = InMemoryAccountRepository()

        signup_input = SignupInput(
            first_name='Eduardo',
            last_name='Cavalcante',
            email='eduardo.cavalcante@example.com',
        )
        signup_use_case = Signup(account_repository=account_repository)
        signup_output = signup_use_case.execute(signup_input)
        assert isinstance(signup_output, SignupOutput)
        assert signup_output.account_id is not None

    def test_should_raise_exception_if_email_already_exists(self):  # noqa: PLR6301
        account_repository = InMemoryAccountRepository()
        account = Account.create(
            name=Name('Eduardo', 'Cavalcante'),
            email=Email('eduardo.cavalcante@example.com'),
        )
        account_repository.save(account)

        signup_input = SignupInput(
            first_name='Eduardo',
            last_name='Cavalcante',
            email='eduardo.cavalcante@example.com',
        )
        signup_use_case = Signup(account_repository=account_repository)

        with pytest.raises(EmailAlreadyExistsException):
            signup_use_case.execute(signup_input)
