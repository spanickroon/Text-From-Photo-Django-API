from django.core.mail import EmailMessage

from apps.order.models import Order


class MailerService:
    @staticmethod
    def send_message(order_id: int) -> None:
        order = Order.objects.get(pk=order_id)
        user_name = order.userprofile.user.username
        user_email = order.userprofile.user.email

        mail = EmailMessage(
            subject="New image order",
            body=(
                f"Hello, {user_name}\n\nYour order from {order.date} to {order.image.name}\n\n\n"
                f"Text from file:\n\n{order.text}"
            ),
            to=[user_email],
            attachments=[(order.image.name, order.image.read(), "application/png")],
        )

        mail.send()

        order.status = order.SENT
        order.save()
