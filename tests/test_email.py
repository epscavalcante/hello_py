import pytest

from app.domain.exceptions.invalid_email import InvalidEmailException
from app.domain.value_objects.email import Email


class TestEmail:
    def test_should_create_valid_email(self):  # noqa: PLR6301
        email = Email('eduardo@email.com')
        assert str(email) == 'eduardo@email.com'

    def test_should_normalize_to_lowercase(self):  # noqa: PLR6301
        email = Email('Eduardo@Email.com')
        assert str(email) == 'eduardo@email.com'

    def test_should_raise_when_missing_at(self):  # noqa: PLR6301
        with pytest.raises(InvalidEmailException):
            Email('eduardoemail.com')

    def test_should_raise_when_missing_domain(self):  # noqa: PLR6301
        with pytest.raises(InvalidEmailException):
            Email('eduardo@')

    def test_should_raise_when_empty(self):  # noqa: PLR6301
        with pytest.raises(InvalidEmailException):
            Email('')

    def test_should_be_equal_when_values_are_equal(self):  # noqa: PLR6301
        email1 = Email('eduardo@email.com')
        email2 = Email('eduardo@email.com')

        assert email1 == email2

    def test_should_not_be_equal_when_values_are_different(self):  # noqa: PLR6301
        email1 = Email('eduardo@email.com')
        email2 = Email('outro@email.com')

        assert email1 != email2
