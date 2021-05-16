from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class OrderAPIView(APIView):
    #serializer_class = OrderSerializer

    def post(self, request: Request) -> Response:
        #serializer = self.serializer_class(data=request.data)
        return Response(status=status.HTTP_200_OK)
