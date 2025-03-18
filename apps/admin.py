from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import User, Project, Task


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = 'username', 'role', 'user_type', 'created_at',
    list_editable = 'role', 'user_type',
    list_filter = 'role', 'user_type',
    pass


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = 'name', 'description', 'created_at',
    pass


@admin.register(Task)
class TaskAdmin(ModelAdmin):
    pass
