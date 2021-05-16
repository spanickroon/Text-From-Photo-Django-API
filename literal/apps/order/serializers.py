from rest_framework import serializers

from .models import Order
from .validators import FileValidator


class OrderSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        required=True,
        validators=[
            FileValidator.image_validator,
        ],
    )

    class Meta:
        model = Order
        fields = ["image"]
