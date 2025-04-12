from django.urls import path, include

from apps.serializers import LoginUserModelSerializer
from apps.views import LoginAPIView, UserRegisterCreateView

urlpatterns = [
    path('register/', UserRegisterCreateView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
]
