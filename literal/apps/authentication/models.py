from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    quantity_orders = models.IntegerField(default=0, null=False)

    def __str__(self) -> str:
        return f"{self.user.username}"
