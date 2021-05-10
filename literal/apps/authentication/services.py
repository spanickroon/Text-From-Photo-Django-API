from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

from .dto import AuthenticationDTO, RegisterDTO, LoginDTO
from .exceptions import (
    UserDoesNotExists,
    UserAlreadyExists,
    TokenDoesNotExists,
    TokenForUserAlreadyExists,
)
from .constants import (
    USER_DOES_NOT_EXISTS_ERROR_MESSAGE,
    USER_ALREADY_EXISTS_ERROR_MESSAGE,
    TOKEN_DOES_NOT_EXISTS_ERROR_MESSAGE,
    TOKEN_FOR_USER_ALREADY_EXISTS_ERROR_MESSAGE,
)


class AuthenticationServices:
    @staticmethod
    def register(data: AuthenticationDTO) -> RegisterDTO:
        if User.objects.filter(username=data.username).exists():
            raise UserAlreadyExists(USER_ALREADY_EXISTS_ERROR_MESSAGE)

        user = User.objects.create_user(
            username=data.username, password=data.password, email=data.email
        )

        if not Token.objects.filter(user=user).exists():
            raise TokenForUserAlreadyExists(TOKEN_FOR_USER_ALREADY_EXISTS_ERROR_MESSAGE)

        token = Token.objects.create(user=user)

        return RegisterDTO(username=user.username, token=token.key)

    @staticmethod
    def login(data: AuthenticationDTO) -> LoginDTO:
        if not User.objects.filter(
            username=data.username, password=data.password
        ).exists():
            raise UserDoesNotExists(USER_DOES_NOT_EXISTS_ERROR_MESSAGE)

        user = User.objects.get(username=data.username, password=data.password)

        if not Token.objects.filter(user=user).exists():
            raise TokenDoesNotExists(TOKEN_DOES_NOT_EXISTS_ERROR_MESSAGE)

        token = Token.objects.get(user=user)

        return LoginDTO(username=user.username, token=token.key)
