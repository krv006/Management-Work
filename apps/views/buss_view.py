from drf_spectacular.utils import extend_schema
from rest_framework.generics import ListCreateAPIView

from apps.models import City, Bus, BusStation, BusCompany, Trip, Seat, Ticket
from apps.serializers.buss_serializer import CityModelSerializer, BusModelSerializer, BusStationModelSerializer, \
    BusCompanyModelSerializer, TripModelSerializer, SeatModelSerializer, TicketModelSerializer


@extend_schema(tags=['Buss'])
class CityListCreateView(ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CityModelSerializer


@extend_schema(tags=['Buss'])
class BussListCreateView(ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusModelSerializer


@extend_schema(tags=['Buss'])
class BusCompanyListCreateView(ListCreateAPIView):
    queryset = BusCompany.objects.all()
    serializer_class = BusCompanyModelSerializer


@extend_schema(tags=['Buss'])
class BusStationListCreateView(ListCreateAPIView):
    queryset = BusStation.objects.all()
    serializer_class = BusStationModelSerializer


@extend_schema(tags=['Buss'])
class TripListCreateView(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripModelSerializer


@extend_schema(tags=['Buss'])
class SeatListCreateView(ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatModelSerializer


@extend_schema(tags=['Buss'])
class TicketListCreateView(ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketModelSerializer
