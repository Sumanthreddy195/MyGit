from django.urls import path
from .views import PayloadAPIView

urlpatterns = [
    path('payload/', PayloadAPIView.as_view(), name='payload_api'),
]
