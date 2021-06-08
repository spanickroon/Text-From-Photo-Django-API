from logging import getLogger

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import UserProfileDoesNotExists
from .serializers import OrderSerializerRequest, OrderSerializerResponse
from .services import OrderService


class OrderAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    request_serializer_class = OrderSerializerRequest
    response_serializer_class = OrderSerializerResponse

    def post(self, request: Request) -> Response:
        serializer = self.request_serializer_class(data=request.data)

        if serializer.is_valid():
            try:
                OrderService.create_order(file=request.FILES["image"], request=request)
            except UserProfileDoesNotExists as exc:
                getLogger(name=__name__).error(msg=str(exc))
                return Response(
                    status=status.HTTP_400_BAD_REQUEST, data=serializer.errors
                )
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def get(self, request: Request) -> Response:
        serializer = self.response_serializer_class(
            data=OrderService.get_orders_by_user(user_id=request.user.pk), many=True
        )

        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
