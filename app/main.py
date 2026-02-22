from http import HTTPStatus

from fastapi import Depends, FastAPI
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from app.application.use_cases.signup.signup import Signup
from app.application.use_cases.signup.signup_input import SignupInput
from app.infraestructure.database.session import get_session
from app.infraestructure.repositories.account import (
    SqlAlchemyAccountRepository,
)

app = FastAPI()


class HelloResponse(BaseModel):
    message: str


class SignupResponse(BaseModel):
    account_id: str


class SignupRequest(BaseModel):
    first_name: str
    last_name: str
    name: str
    email: EmailStr


@app.get('/', status_code=HTTPStatus.OK, response_model=HelloResponse)
async def hello_world() -> HelloResponse:
    return HelloResponse(message='Hello, World!')


@app.post(
    '/signup', status_code=HTTPStatus.CREATED, response_model=SignupResponse
)
async def signup(
    request: SignupRequest, session: Session = Depends(get_session)
) -> SignupResponse:
    """
    Endpoint for user signup.
    """
    account_repo = SqlAlchemyAccountRepository(session)
    signup_input = SignupInput(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
    )
    use_case = Signup(account_repo)
    signup_output = await use_case.execute(signup_input)

    return SignupResponse(account_id=signup_output.account_id)
