from django.contrib.auth.models import User
from rest_framework import serializers, validators

from .validators import AuthenticationValidator


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        max_length=30,
        min_length=5,
        validators=[
            AuthenticationValidator.text_validator,
            validators.UniqueValidator(queryset=User.objects.all()),
        ],
        style={"placeholder": "Username"},
    )
    email = serializers.EmailField(
        required=True,
        style={"input_type": "email", "placeholder": "Email"},
    )
    password = serializers.CharField(
        required=True,
        max_length=30,
        min_length=5,
        validators=[
            AuthenticationValidator.text_validator,
        ],
        style={"input_type": "password", "placeholder": "Password"},
    )

    class Meta:
        model = User
        fields = ["username", "email", "password"]


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        max_length=30,
        min_length=5,
        validators=[
            AuthenticationValidator.text_validator,
        ],
        style={"placeholder": "Username"},
    )
    password = serializers.CharField(
        required=True,
        max_length=30,
        min_length=5,
        validators=[
            AuthenticationValidator.text_validator,
        ],
        style={"input_type": "password", "placeholder": "Password"},
    )

    class Meta:
        model = User
        fields = ["username", "password"]
