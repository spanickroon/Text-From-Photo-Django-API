from unittest import mock

from django.test import TestCase
from parameterized import param, parameterized
from rest_framework import validators

from apps.order.constants import (
    EXTENSION_ERROR_MESSAGE,
    MAX_IMAGE_SIZE,
    MAX_IMAGE_SIZE_ERROR_MESSAGE,
)
from apps.order.validators import FileValidator


class FileValidatorTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.validator = FileValidator

    def test__image_validator__success(self):
        file = mock.MagicMock()
        file.name = "test.jpg"
        file.size = 1

        actual_file = self.validator.image_validator(file=file)
        self.assertEqual(actual_file.name, file.name)
        self.assertEqual(actual_file.size, file.size)

    @parameterized.expand(
        [
            param(
                EXTENSION_ERROR_MESSAGE,
                name="test.pdf",
                size=1,
                error=validators.ValidationError,
            ),
            param(
                MAX_IMAGE_SIZE_ERROR_MESSAGE,
                name="test.jpg",
                size=MAX_IMAGE_SIZE + 1,
                error=validators.ValidationError,
            ),
        ]
    )
    def test__image_validator__raise_exceptions(self, _, name, size, error):
        file = mock.MagicMock()
        file.name = name
        file.size = size

        with self.assertRaises(error):
            self.validator.image_validator(file=file)
