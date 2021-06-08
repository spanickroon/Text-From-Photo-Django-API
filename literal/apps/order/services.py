from time import sleep

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models.query import QuerySet
from rest_framework.request import Request

from apps.mailer.services import MailerService
from apps.scanner.services import ScannerService
from literal.celery import app

from .constants import USER_PROFILE_ERROR
from .exceptions import UserProfileDoesNotExists
from .models import Order, UserProfile


@app.task
def order_task(order_id: int) -> None:
    sleep(1)
    ScannerService.scan_image(order_id=order_id)
    MailerService.send_message(order_id=order_id)


class OrderService:
    @staticmethod
    def create_order(file: InMemoryUploadedFile, request: Request) -> None:
        try:
            userprofile = UserProfile.objects.get(user=request.user)
            order = Order.objects.create(
                userprofile=userprofile,
                image=file,
                extension=file.name[file.name.rindex(".") :],
            )
            userprofile.quantity_orders += 1
            userprofile.save()
        except UserProfile.DoesNotExist:
            raise UserProfileDoesNotExists(USER_PROFILE_ERROR)
        order_task.delay(order_id=order.pk)

    @staticmethod
    def get_orders_by_user(user_id: int) -> list:
        return list(Order.objects.filter(userprofile__user_id=user_id).values())
