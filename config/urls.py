from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from config.swagger import urlpatterns as swagger_patterns
from config import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", include("apps.user.urls")),
    path("api/v1/music/", include("apps.music.urls")),
]
urlpatterns += swagger_patterns
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
