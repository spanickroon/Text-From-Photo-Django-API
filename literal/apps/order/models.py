from django.db import models

from apps.authentication.models import UserProfile


class Order(models.Model):
    ACTIVE = "Active"
    PROCESSING = "Processing"
    SENT = "Sent"
    REJECTED = "Rejected"
    CHOICES = (
        (ACTIVE, "Active"),
        (PROCESSING, "Processing"),
        (SENT, "Sent"),
        (REJECTED, "Rejected"),
    )

    userprofile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="orders"
    )

    date = models.DateTimeField(auto_now=True, null=False)
    image = models.ImageField(null=False, upload_to="files/")
    status = models.CharField(max_length=30, choices=CHOICES, default=ACTIVE)
    text = models.TextField(null=True)

    extension = models.CharField(max_length=10, null=True)

    def __str__(self) -> str:
        return f"{self.userprofile.user.username} - {self.date} - {self.image.name}"
