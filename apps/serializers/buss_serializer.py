from rest_framework.serializers import ModelSerializer

from apps.models import City, BusStation, BusCompany, Bus, Trip, Seat, Ticket
from apps.serializers import UserModelSerializer


class CityModelSerializer(ModelSerializer):
    class Meta:
        model = City
        fields = 'id', 'name',


class BusStationModelSerializer(ModelSerializer):
    class Meta:
        model = BusStation
        fields = 'id', 'name', 'city',

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['city'] = CityModelSerializer(instance.city).data if instance.city else None
        return repr


class BusCompanyModelSerializer(ModelSerializer):
    class Meta:
        model = BusCompany
        fields = 'id', 'name', 'contact_phone',


class BusModelSerializer(ModelSerializer):
    class Meta:
        model = Bus
        fields = 'id', 'model', 'company', 'seat_count', 'plate_number',

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['company'] = BusCompanyModelSerializer(instance.company).data if instance.company else None
        return repr


class TripModelSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = 'id', 'bus', 'departure_station', 'arrival_station', 'departure_time', 'arrival_time', 'price',

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['bus'] = BusModelSerializer(instance.bus).data if instance.bus else None
        repr['departure_station'] = BusStationModelSerializer(
            instance.departure_station).data if instance.departure_station else None
        repr['arrival_station'] = BusStationModelSerializer(
            instance.arrival_station).data if instance.arrival_station else None
        return repr


class SeatModelSerializer(ModelSerializer):
    class Meta:
        model = Seat
        fields = 'id', 'trip', 'seat_number', 'is_reserved',

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['trip'] = TripModelSerializer(instance.trip).data if instance.trip else None
        return


class TicketModelSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = 'id', 'user', 'trip', 'seat', 'booked_at', 'is_paid',

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['user'] = UserModelSerializer(instance.user).data if instance.user else None
        repr['trip'] = TripModelSerializer(instance.trip).data if instance.trip else None
        repr['seat'] = SeatModelSerializer(instance.seat).data if instance.seat else None
        return repr
