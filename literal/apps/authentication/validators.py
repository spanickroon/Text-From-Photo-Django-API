import string

from rest_framework import validators

from .constants import USERNAME_VALIDATOR_ERROR_MESSAGE


class AuthenticationValidator:
    @staticmethod
    def text_validator(value: str) -> str:
        if bool(set(value) - set(string.ascii_letters + string.digits)):
            raise validators.ValidationError(USERNAME_VALIDATOR_ERROR_MESSAGE)
        return value
