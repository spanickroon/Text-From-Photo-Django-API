from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .dto import AuthenticationDTO
from .exceptions import (
    TokenDoesNotExists,
    TokenForUserAlreadyExists,
    UserAlreadyExists,
    UserDoesNotExists,
)
from .serializers import LoginSerializer, RegisterSerializer
from .services import AuthenticationServices


class RegisterAPIView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            try:
                register_data = AuthenticationServices.register(
                    data=AuthenticationDTO(**serializer.data)
                )
            except (UserAlreadyExists, TokenForUserAlreadyExists) as exc:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST, data={"message": str(exc)}
                )
            return Response(status=status.HTTP_200_OK, data=register_data.dict())

        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            try:
                login_data = AuthenticationServices.login(
                    data=AuthenticationDTO(**serializer.data)
                )
            except (UserDoesNotExists, TokenDoesNotExists) as exc:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST, data={"message": str(exc)}
                )
            return Response(status=status.HTTP_200_OK, data=login_data.dict())

        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
