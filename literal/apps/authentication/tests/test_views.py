from unittest import mock

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from apps.authentication.constants import (
    TOKEN_DOES_NOT_EXISTS_ERROR_MESSAGE,
    USER_DOES_NOT_EXISTS_ERROR_MESSAGE,
)


class RegisterAPIViewTestCase(APITestCase):
    def setUp(self) -> None:
        super().setUp()

        self.authentication_url = reverse("register")

    def test__register__success(self):
        response = self.client.post(
            self.authentication_url,
            data={
                "username": "testuser",
                "email": "test@test.com",
                "password": "testpass",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "testuser")
        self.assertIsNotNone(response.data["token"])

    def test__register__validator_errors(self):
        response = self.client.post(
            self.authentication_url,
            data={"username": "", "email": "", "password": ""},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginAPIViewTestCase(APITestCase):
    def setUp(self) -> None:
        super().setUp()

        self.authentication_url = reverse("login")

    def test__register__success(self):
        user = User.objects.create_user(
            username="testuser", email="test@test.com", password="testpass"
        )
        Token.objects.create(user=user)

        response = self.client.post(
            self.authentication_url,
            data={"username": "testuser", "password": "testpass"},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "testuser")
        self.assertIsNotNone(response.data["token"])

    def test__register__validator_errors(self):
        response = self.client.post(
            self.authentication_url,
            data={"username": "", "password": ""},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @mock.patch("apps.authentication.views.getLogger")
    def test__register__raise_exception_user(self, logger_mock):
        response = self.client.post(
            self.authentication_url,
            data={"username": "testuser", "password": "testpass"},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["message"], USER_DOES_NOT_EXISTS_ERROR_MESSAGE)

        self.assertTrue(logger_mock.called)

    @mock.patch("apps.authentication.views.getLogger")
    def test__register__raise_exception_token(self, logger_mock):
        User.objects.create_user(
            username="testuser", email="test@test.com", password="testpass"
        )

        response = self.client.post(
            self.authentication_url,
            data={"username": "testuser", "password": "testpass"},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["message"], TOKEN_DOES_NOT_EXISTS_ERROR_MESSAGE)

        self.assertTrue(logger_mock.called)
