from rest_framework import serializers

from .models import Order
from .validators import FileValidator


class OrderSerializerRequest(serializers.ModelSerializer):
    image = serializers.ImageField(
        required=True,
        validators=[
            FileValidator.image_validator,
        ],
    )

    class Meta:
        model = Order
        fields = ["image"]


class OrderSerializerResponse(serializers.ModelSerializer):
    userprofile_id = serializers.IntegerField()
    image = serializers.CharField()

    class Meta:
        model = Order
        fields = ["userprofile_id", "date", "status", "text", "image"]
