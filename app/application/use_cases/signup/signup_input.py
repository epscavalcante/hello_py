from dataclasses import dataclass


@dataclass(frozen=True)
class SignupInput:
    first_name: str
    last_name: str
    email: str
