from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.request import Request

from apps.mailer.services import MailerService
from apps.scanner.services import ScannerService

from .constants import USER_PROFILE_ERROR
from .exceptions import UserProfileDoesNotExists
from .models import Order, UserProfile


class OrderService:
    @staticmethod
    def create_order(file: InMemoryUploadedFile, request: Request) -> None:
        try:
            userprofile = UserProfile.objects.get(user=request.user)
            order = Order.objects.create(userprofile=userprofile, image=file)
            userprofile.quantity_orders += 1
            userprofile.save()
        except UserProfile.DoesNotExist:
            raise UserProfileDoesNotExists(USER_PROFILE_ERROR)

        ScannerService.scan_image(order_id=order.pk)
        MailerService.send_message(order_id=order.pk)
