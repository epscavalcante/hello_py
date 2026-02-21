from app.domain.exceptions.domain import DomainException
from app.domain.value_objects.email import Email


class EmailAlreadyExistsException(DomainException):
    def __init__(self, email: Email):
        self.email = email
        super().__init__(f"Email '{email}' already exists.")

    def __str__(self):
        return f"Email '{self.email}' already exists."
