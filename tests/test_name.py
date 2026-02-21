import pytest

from app.domain.exceptions.invalid_name import InvalidNameException
from app.domain.value_objects.name import Name


class TestName:
    def test_should_create_valid_name(self):  # noqa: PLR6301
        first_name = 'Eduardo'
        last_name = 'Cavalcante'
        name = Name(first_name, last_name)
        assert str(name) == 'Eduardo Cavalcante'
        assert name.first_name == 'Eduardo'
        assert name.last_name == 'Cavalcante'

    def test_should_trim_spaces(self):  # noqa: PLR6301
        name = Name('  Eduardo  ', '  Cavalcante  ')
        assert str(name) == 'Eduardo Cavalcante'

    def test_should_raise_when_empty(self):  # noqa: PLR6301
        with pytest.raises(InvalidNameException):
            Name('', '')

    def test_should_raise_when_only_spaces(self):  # noqa: PLR6301
        with pytest.raises(InvalidNameException):
            Name('   ', '   ')

    def test_should_be_equal_when_values_are_equal(self):  # noqa: PLR6301
        name1 = Name('Eduardo', 'Cavalcante')
        name2 = Name('Eduardo', 'Cavalcante')

        assert name1 == name2

    def test_should_not_be_equal_when_values_are_different(self):  # noqa: PLR6301
        name1 = Name('Eduardo', 'Cavalcante')
        name2 = Name('Carlos', 'Silva')

        assert name1 != name2
