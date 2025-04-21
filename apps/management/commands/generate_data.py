from decimal import Decimal
from random import randint, choice

from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand
from django.utils.timezone import now, timedelta
from faker import Faker

from apps.models import City, BusStation, BusCompany, Bus, Trip, Seat, Ticket, User


class Command(BaseCommand):
    help = "Generate fake data for bus app"
    f = Faker()

    def add_arguments(self, parser):
        parser.add_argument('--cities', type=int, default=5)
        parser.add_argument('--stations', type=int, default=10)
        parser.add_argument('--companies', type=int, default=5)
        parser.add_argument('--buses', type=int, default=10)
        parser.add_argument('--trips', type=int, default=20)
        parser.add_argument('--users', type=int, default=10)
        parser.add_argument('--tickets', type=int, default=20)

    def handle(self, *args, **options):
        cities = [City.objects.create(name=self.f.city()) for _ in range(options['cities'])]

        stations = [BusStation.objects.create(name=self.f.street_name(), city=choice(cities))
                    for _ in range(options['stations'])]

        companies = [BusCompany.objects.create(name=self.f.company(),
                                               contact_phone=f'+998{randint(900000000, 999999999)}')
                     for _ in range(options['companies'])]

        buses = [Bus.objects.create(company=choice(companies),
                                    model=self.f.word(),
                                    seat_count=randint(20, 60),
                                    plate_number=self.f.license_plate())
                 for _ in range(options['buses'])]

        users = [User.objects.create(email=self.f.email(),
                                     password=make_password('password123'))
                 for _ in range(options['users'])]

        trips = []
        for _ in range(options['trips']):
            departure, arrival = self.f.random_elements(elements=stations, length=2, unique=True)
            departure_time = now() + timedelta(days=randint(1, 10))
            arrival_time = departure_time + timedelta(hours=randint(1, 10))
            price = Decimal(str(randint(50000, 150000)))
            trip = Trip.objects.create(
                bus=choice(buses),
                departure_station=departure,
                arrival_station=arrival,
                departure_time=departure_time,
                arrival_time=arrival_time,
                price=price
            )
            trips.append(trip)
            for i in range(1, trip.bus.seat_count + 1):
                Seat.objects.create(trip=trip, seat_number=i)

        for _ in range(options['tickets']):
            trip = choice(trips)
            free_seats = trip.seats.filter(is_reserved=False)
            if not free_seats.exists():
                continue
            seat = free_seats.order_by('?').first()
            user = choice(users)
            Ticket.objects.create(user=user, trip=trip, seat=seat, is_paid=self.f.boolean())

        self.stdout.write(self.style.SUCCESS("Fake data qoshildi"))
