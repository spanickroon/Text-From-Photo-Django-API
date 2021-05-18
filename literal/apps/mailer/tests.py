from tempfile import TemporaryFile
from unittest import mock

from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.test import TestCase

from apps.authentication.models import UserProfile
from apps.order.models import Order

from .services import MailerService


class MailerServiceTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.service = MailerService

        self.user = User.objects.create_user(
            username="test", email="test@test.com", password="test"
        )
        self.userprofile = UserProfile.objects.create(user=self.user)
        self.image_file = InMemoryUploadedFile(
            name="test_image.jpg",
            content_type="image/jpeg",
            file=TemporaryFile(),
            charset=None,
            field_name="test",
            size=1,
        )

        self.order = Order.objects.create(
            userprofile=self.userprofile,
            image=self.image_file,
            extension=self.image_file.name[self.image_file.name.rindex(".") :],
        )

    @mock.patch("apps.mailer.services.EmailMessage.send")
    def test__send_message__success(self, mailer_mock):
        self.service.send_message(order_id=self.order.pk)
        self.assertTrue(mailer_mock.called)
