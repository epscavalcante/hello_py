import pytest

from app.domain.exceptions.invalid_document import InvalidDocumentException
from app.domain.value_objects.document import Document


class TestDocument:
    def test_should_create_valid_document(self):  # noqa: PLR6301
        document = Document('52998224725')
        assert str(document) == '52998224725'

    @pytest.mark.parametrize(
        'invalid_value',
        [
            '',  # vazio
            '123',  # tamanho menor
            '123456789012',  # tamanho maior
            '1234567890A',  # caractere não numérico
            '00000000000',  # sequência repetida
            '11111111111',
            '22222222222',
        ],
    )
    def test_should_raise_invalid_cpf_for_invalid_values(self, invalid_value):  # noqa: PLR6301
        with pytest.raises(InvalidDocumentException):
            Document(invalid_value)

    def test_should_be_equal_when_values_are_equal(self):  # noqa: PLR6301
        cpf1 = Document('52998224725')
        cpf2 = Document('52998224725')

        assert cpf1 == cpf2

    def test_should_not_be_equal_when_values_are_different(self):  # noqa: PLR6301
        cpf1 = Document('52998224725')
        cpf2 = Document('86960752000')

        assert cpf1 != cpf2
