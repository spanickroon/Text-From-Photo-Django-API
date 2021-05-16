from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.request import Request

from .constants import USER_PROFILE_ERROR
from .exceptions import UserProfileDoesNotExists
from .models import Order, UserProfile


class OrderService:
    @staticmethod
    def create_order(file: InMemoryUploadedFile, request: Request) -> None:
        try:
            Order.objects.create(
                userprofile=UserProfile.objects.get(user=request.user), image=file
            )
        except UserProfile.DoesNotExist:
            raise UserProfileDoesNotExists(USER_PROFILE_ERROR)
