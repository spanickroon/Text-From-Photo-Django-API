from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .constants import (
    TOKEN_DOES_NOT_EXISTS_ERROR_MESSAGE,
    TOKEN_FOR_USER_ALREADY_EXISTS_ERROR_MESSAGE,
    USER_ALREADY_EXISTS_ERROR_MESSAGE,
    USER_DOES_NOT_EXISTS_ERROR_MESSAGE,
)
from .dto import AuthenticationDTO, LoginDTO, RegisterDTO
from .exceptions import (
    TokenDoesNotExists,
    TokenForUserAlreadyExists,
    UserAlreadyExists,
    UserDoesNotExists,
)
from .models import UserProfile


class AuthenticationServices:
    @staticmethod
    def register(data: AuthenticationDTO) -> RegisterDTO:
        if User.objects.filter(username=data.username).exists():
            raise UserAlreadyExists(USER_ALREADY_EXISTS_ERROR_MESSAGE)

        user = User.objects.create_user(
            username=data.username, password=data.password, email=data.email
        )

        UserProfile.objects.create(user=user)

        if Token.objects.filter(user=user).exists():
            raise TokenForUserAlreadyExists(TOKEN_FOR_USER_ALREADY_EXISTS_ERROR_MESSAGE)

        token = Token.objects.create(user=user)

        return RegisterDTO(username=user.username, token=token.key)

    @staticmethod
    def login(data: AuthenticationDTO) -> LoginDTO:
        user = authenticate(username=data.username, password=data.password)

        if user is None:
            raise UserDoesNotExists(USER_DOES_NOT_EXISTS_ERROR_MESSAGE)

        if not Token.objects.filter(user=user).exists():
            raise TokenDoesNotExists(TOKEN_DOES_NOT_EXISTS_ERROR_MESSAGE)

        token = Token.objects.get(user=user)

        return LoginDTO(username=user.username, token=token.key)
