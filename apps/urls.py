from django.urls import path, include

from apps.views import LoginAPIView, UserRegisterCreateView, UserListAPIView
from apps.views.buss_view import CityListCreateView, BussListCreateView, BusCompanyListCreateView, \
    BusStationListCreateView, TripListCreateView, SeatListCreateView, TicketListCreateView
from apps.views.site_view import SiteListCreateAPIView, QuestionListCreateAPIView, AnswerListCreateAPIView

urlpatterns = [
    path('register/', UserRegisterCreateView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('user/', UserListAPIView.as_view(), name='user-list'),
    path('site/', SiteListCreateAPIView.as_view(), name='site'),
    path('question/', QuestionListCreateAPIView.as_view(), name='question'),
    path('answer/', AnswerListCreateAPIView.as_view(), name='answer'),
    path('city/', CityListCreateView.as_view(), name='city'),
    path('buss/', BussListCreateView.as_view(), name='buss'),
    path('buss-company/', BusCompanyListCreateView.as_view(), name='buss_company'),
    path('buss-station/', BusStationListCreateView.as_view(), name='buss_station'),
    path('trip/', TripListCreateView.as_view(), name='trip'),
    path('seat/', SeatListCreateView.as_view(), name='seat'),
    path('ticket/', TicketListCreateView.as_view(), name='ticket'),

]
