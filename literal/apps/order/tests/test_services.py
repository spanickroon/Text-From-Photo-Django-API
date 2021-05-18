from tempfile import TemporaryFile
from unittest import mock

from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.test import TestCase

from apps.authentication.models import UserProfile
from apps.order.exceptions import UserProfileDoesNotExists
from apps.order.models import Order
from apps.order.services import OrderService


class OrderServiceTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.service = OrderService

        self.image_file = InMemoryUploadedFile(
            name="test_image.jpg",
            content_type="image/jpeg",
            file=TemporaryFile(),
            charset=None,
            field_name="test",
            size=1,
        )

        self.user = User.objects.create_user(username="test", password="test")

    @mock.patch("apps.order.services.order_task.delay")
    def test__create_order__success(self, mock_task):
        UserProfile.objects.create(user=self.user)

        request_mock = mock.MagicMock()
        request_mock.user = self.user

        self.service.create_order(file=self.image_file, request=request_mock)

        userprofile = UserProfile.objects.get(user=self.user)
        order = Order.objects.get(userprofile=userprofile)

        self.assertEqual(userprofile.quantity_orders, 1)
        self.assertEqual(order.status, Order.ACTIVE)
        self.assertEqual(order.userprofile, userprofile)
        self.assertEqual(order.extension, ".jpg")

        self.assertTrue(mock_task.called)
        mock_task.called_once_with(order_id=order.pk)

    def test__test__create_order__raise_exception(self):
        request_mock = mock.MagicMock()
        request_mock.user = self.user

        with self.assertRaises(UserProfileDoesNotExists):
            self.service.create_order(file=self.image_file, request=request_mock)
