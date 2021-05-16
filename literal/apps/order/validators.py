from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import validators

from .constants import (
    ALLOWED_EXTENSIONS,
    EXTENSION_ERROR_MESSAGE,
    MAX_IMAGE_SIZE,
    MAX_IMAGE_SIZE_ERROR_MESSAGE,
)


class FileValidator:
    @staticmethod
    def image_validator(file: InMemoryUploadedFile) -> InMemoryUploadedFile:
        extension = file.name[file.name.rindex(".") :]
        if extension not in ALLOWED_EXTENSIONS:
            raise validators.ValidationError(EXTENSION_ERROR_MESSAGE)
        if file.size > MAX_IMAGE_SIZE:
            raise validators.ValidationError(MAX_IMAGE_SIZE_ERROR_MESSAGE)
        return file
