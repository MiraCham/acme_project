from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

app_name = 'birthday'

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
