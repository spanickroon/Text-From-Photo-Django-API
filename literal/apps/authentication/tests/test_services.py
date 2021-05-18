from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.authtoken.models import Token

from apps.authentication.dto import AuthenticationDTO
from apps.authentication.services import AuthenticationServices


class AuthenticationServicesTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.service = AuthenticationServices

    def test__register__success(self):
        actual_dto = self.service.register(
            data=AuthenticationDTO(
                username="test", email="test@test.com", password="test"
            )
        )

        self.assertEqual(actual_dto.username, "test")
        self.assertIsNotNone(actual_dto.token)

    def test__login__success(self):
        user = User.objects.create_user(
            username="test", email="test@test.com", password="test"
        )
        token = Token.objects.create(user=user)

        actual_dto = self.service.login(
            data=AuthenticationDTO(
                username=user.username,
                password="test",
            )
        )

        self.assertEqual(actual_dto.username, user.username)
        self.assertEqual(actual_dto.token, token.key)
