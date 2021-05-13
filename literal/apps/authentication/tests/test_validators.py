from django.test import TestCase
from parameterized import param, parameterized
from rest_framework.validators import ValidationError

from apps.authentication.validators import AuthenticationValidator


class AuthenticationValidatorTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.validators = AuthenticationValidator

    @parameterized.expand(
        [
            param("test_validator_value_1", value="12345", expected_value="12345"),
            param(
                "test_validator_value_2",
                value="sdfsdfsdfsdf",
                expected_value="sdfsdfsdfsdf",
            ),
            param(
                "test_validator_value_3",
                value="8hnjsi48h8h1",
                expected_value="8hnjsi48h8h1",
            ),
            param(
                "test_validator_value_4",
                value="dfsdf12312312",
                expected_value="dfsdf12312312",
            ),
            param(
                "test_validator_value_5",
                value="1k1i23mk12gg",
                expected_value="1k1i23mk12gg",
            ),
        ]
    )
    def test__text_validator__success(self, _, value, expected_value):
        self.assertEqual(self.validators.text_validator(value), expected_value)

    @parameterized.expand(
        [
            param("sdfsdffdsf", value="_________"),
            param("test_validator_value_2", value="sdfsdf***jsidf"),
            param("test_validator_value_3", value="/@!sdf"),
            param("test_validator_value_4", value="123123__sdaksoda"),
            param("test_validator_value_5", value="8213hhns()"),
        ]
    )
    def test__text_validator__raise_exception(self, _, value):
        with self.assertRaises(ValidationError):
            self.validators.text_validator(value)
