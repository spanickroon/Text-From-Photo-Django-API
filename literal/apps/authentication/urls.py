from django.urls import path

from .views import LoginAPIView, RegisterAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view()),
    path("register/", RegisterAPIView.as_view()),
]
