from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-authentication/", include("rest_framework.urls")),
    path("api/v1/authentication/", include("apps.authentication.urls")),
    path("api/v1/order/", include("apps.order.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
