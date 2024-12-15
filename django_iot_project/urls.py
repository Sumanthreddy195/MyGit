from django.contrib import admin
from django.urls import path, include
from devices import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('api/', include('devices.urls')),  # Include devices app URLs
]
