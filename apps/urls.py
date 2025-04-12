from django.urls import path, include

from apps.serializers import LoginUserModelSerializer
from apps.views import LoginAPIView, UserRegisterCreateView, UserListAPIView

urlpatterns = [
    path('register/', UserRegisterCreateView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('user/', UserListAPIView.as_view(), name='user-list'),
]
