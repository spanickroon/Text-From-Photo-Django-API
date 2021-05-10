import typing

from pydantic import BaseModel


class AuthenticationDTO(BaseModel):
    username: typing.Optional[str]
    email: typing.Optional[str]
    token: typing.Optional[str]
    password: typing.Optional[str]


class RegisterDTO(BaseModel):
    username: str
    token: str


class LoginDTO(BaseModel):
    username: str
    token: str
