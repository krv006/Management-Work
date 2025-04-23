from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from apps.models import City, Bus, BusStation, BusCompany, Trip, Seat, Ticket
from apps.serializers.buss_serializer import CityModelSerializer, BusModelSerializer, BusStationModelSerializer, \
    BusCompanyModelSerializer, TripModelSerializer, SeatModelSerializer, TicketModelSerializer


@extend_schema(tags=['Buss'])
class CityListCreateView(ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CityModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['Buss'])
class BussListCreateView(ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['Buss'])
class BusCompanyListCreateView(ListCreateAPIView):
    queryset = BusCompany.objects.all()
    serializer_class = BusCompanyModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['Buss'])
class BusStationListCreateView(ListCreateAPIView):
    queryset = BusStation.objects.all()
    serializer_class = BusStationModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['Buss'])
class TripListCreateView(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['Buss'])
class SeatListCreateView(ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatModelSerializer
    permission_classes = AllowAny,


@extend_schema(tags=['Buss'])
class TicketListCreateView(ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer
    permission_classes = AllowAny,
