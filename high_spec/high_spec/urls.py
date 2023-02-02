
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# print(settings.STATIC_URL, settings.STATIC_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('spec/', include('spec_calculator.urls')),
] + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)