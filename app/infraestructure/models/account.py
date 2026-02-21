from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.infraestructure.models.base import BaseModel


class AccountModel(BaseModel):
    __tablename__ = 'accounts'

    account_id: Mapped[str] = mapped_column(String, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    # is_active: Mapped[bool] = mapped_column(Boolean, default=True)
