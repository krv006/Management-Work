from django.core.validators import MinValueValidator, RegexValidator
from django.db.models import CharField, Model, ForeignKey, CASCADE, PositiveIntegerField, DateTimeField, DecimalField, \
    BooleanField, OneToOneField

from apps.models import TimeBasedModel


class City(TimeBasedModel):
    name = CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = "name",

    def __str__(self):
        return self.name


class BusStation(Model):
    name = CharField(max_length=100)
    city = ForeignKey('apps.City', CASCADE)

    class Meta:
        verbose_name = "Bus Station"
        verbose_name_plural = "Bus Stations"
        ordering = "city__name", "name",
        unique_together = "name", "city",

    def __str__(self):
        return f"{self.name} ({self.city.name})"


class BusCompany(Model):
    name = CharField(max_length=100, unique=True)
    contact_phone = CharField(
        max_length=13,
        validators=[RegexValidator(regex=r'^\+998\d{9}$', message="Phone must be in format: +998901234567")],
        help_text="Contact phone in format +998901234567"
    )

    class Meta:
        verbose_name = "Bus Company"
        verbose_name_plural = "Bus Companies"
        ordering = "name",

    def __str__(self):
        return self.name


class Bus(Model):
    company = ForeignKey('apps.BusCompany', CASCADE)
    model = CharField(max_length=100, blank=True, null=True)
    seat_count = PositiveIntegerField(validators=[MinValueValidator(1)], help_text="Number of seats")
    plate_number = CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Bus"
        verbose_name_plural = "Buses"
        ordering = "plate_number",

    def __str__(self):
        return f"{self.model or 'Unknown'} - {self.plate_number}"


class Trip(Model):
    bus = ForeignKey('apps.Bus', CASCADE)
    departure_station = ForeignKey('apps.BusStation', CASCADE, related_name='departure_trips')
    arrival_station = ForeignKey('apps.BusStation', CASCADE, related_name='arrival_trips')
    departure_time = DateTimeField()
    arrival_time = DateTimeField()
    price = DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])

    class Meta:
        verbose_name = "Trip"
        verbose_name_plural = "Trips"
        ordering = "departure_time",

    def save(self, *args, **kwargs):
        if self.arrival_time <= self.departure_time:
            raise ValueError("Arrival time must be after departure time.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.departure_station.city.name} → {self.arrival_station.city.name} ({self.departure_time})"


class Seat(Model):
    trip = ForeignKey('apps.Trip', CASCADE, related_name='seats')
    seat_number = PositiveIntegerField(validators=[MinValueValidator(1)])
    is_reserved = BooleanField(default=False)

    class Meta:
        verbose_name = "Seat"
        verbose_name_plural = "Seats"
        unique_together = "trip", "seat_number",
        ordering = "trip", "seat_number",

    def save(self, *args, **kwargs):
        if self.seat_number > self.trip.bus.seat_count:
            raise ValueError(f"Seat number {self.seat_number} exceeds bus capacity {self.trip.bus.seat_count}.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Trip {self.trip.id} - Seat {self.seat_number}"


class Ticket(TimeBasedModel):
    user = ForeignKey('apps.User', CASCADE)
    trip = ForeignKey('apps.Trip', CASCADE)
    seat = OneToOneField('apps.Seat', CASCADE)
    booked_at = DateTimeField(auto_now_add=True)
    is_paid = BooleanField(default=False)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
        ordering = "-booked_at",

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.seat.is_reserved:
                raise ValueError("This seat is already reserved.")
            self.seat.is_reserved = True
            self.seat.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ticket #{self.id} - {self.user.username} - {self.trip}"
