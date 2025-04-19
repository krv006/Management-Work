from django.contrib import admin
from django.contrib.admin import ModelAdmin
from import_export.admin import ImportExportMixin

from apps.forms import CustomAdminAuthenticationForm
from apps.models import User, SiteSettings, Question, Answer, City, BusStation, BusCompany, Bus, Trip, Seat, Ticket

admin.AdminSite.login_form = CustomAdminAuthenticationForm


@admin.register(User)
class UserAdmin(ImportExportMixin, ModelAdmin):
    list_display = 'username', 'first_name', 'last_name', 'email', 'name', 'is_active',
    list_editable = 'is_active',
    list_filter = 'is_active',


@admin.register(SiteSettings)
class SiteSettingsAdmin(ImportExportMixin, ModelAdmin):
    list_display = 'region_to_region',


@admin.register(Question)
class QuestionAdmin(ImportExportMixin, ModelAdmin):
    list_display = 'text', 'created_at',
    list_filter = 'created_at',


@admin.register(Answer)
class AnswerAdmin(ImportExportMixin, ModelAdmin):
    list_display = 'text', 'question', 'created_at',
    list_filter = 'created_at',


@admin.register(City)
class CityAdmin(ImportExportMixin, ModelAdmin):
    list_display = 'name',


@admin.register(BusStation)
class BusStationAdmin(ImportExportMixin, ModelAdmin):
    list_display = 'name', 'city',
    list_filter = 'city',


@admin.register(BusCompany)
class BusCompanyAdmin(ImportExportMixin, ModelAdmin):
    list_display = 'name', 'contact_phone',


@admin.register(Bus)
class BusAdmin(ImportExportMixin, ModelAdmin):
    list_display = 'company', 'model', 'seat_count', 'plate_number',
    list_filter = 'company',


@admin.register(Trip)
class TripAdmin(ImportExportMixin, ModelAdmin):
    list_display = 'bus', 'arrival_station', 'departure_station', 'departure_time', 'arrival_time', 'price',
    list_filter = 'bus',


@admin.register(Seat)
class SeatAdmin(ImportExportMixin, ModelAdmin):
    list_display = 'trip', 'seat_number', 'is_reserved',
    list_filter = 'trip',


@admin.register(Ticket)
class TicketAdmin(ImportExportMixin, ModelAdmin):
    list_display = 'user', 'trip', 'seat', 'booked_at', 'is_paid',
    list_filter = 'user', 'trip', 'seat',


admin.AdminSite.login_form = CustomAdminAuthenticationForm
