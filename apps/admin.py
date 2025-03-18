from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import User, Project, Task


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = 'username', 'role', 'user_type', 'created_at',
    list_editable = 'role', 'user_type',
    list_filter = 'role', 'user_type',


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = "name", "manager", "manager", "display_team_members", "created_at",
    list_editable = "manager",

    def display_team_members(self, obj):
        return ", ".join([user.username for user in obj.team_members.all()])

    display_team_members.short_description = "Team Members"


@admin.register(Task)
class TaskAdmin(ModelAdmin):
    list_display = 'project', 'title', 'assigned_to', 'status', 'created_at',
    list_editable = 'status', 'assigned_to',
    list_filter = 'title',
