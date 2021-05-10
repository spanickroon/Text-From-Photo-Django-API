from django.test import TestCase

from apps.authentication.services import AuthenticationServices


class AuthenticationServicesTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.service = AuthenticationServices

