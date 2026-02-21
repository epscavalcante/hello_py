from dataclasses import dataclass


@dataclass(frozen=True)
class SignupOutput:
    account_id: str
