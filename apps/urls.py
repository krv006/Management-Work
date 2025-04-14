from django.urls import path, include

from apps.views import LoginAPIView, UserRegisterCreateView, UserListAPIView
from apps.views.site_view import SiteListCreateAPIView, QuestionListCreateAPIView, AnswerListCreateAPIView

urlpatterns = [
    path('register/', UserRegisterCreateView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('user/', UserListAPIView.as_view(), name='user-list'),
    path('site/', SiteListCreateAPIView.as_view(), name='site'),
    path('question/', QuestionListCreateAPIView.as_view(), name='question'),
    path('answer/', AnswerListCreateAPIView.as_view(), name='answer'),
]
