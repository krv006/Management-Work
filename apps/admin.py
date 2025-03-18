from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import User, Project, Task


@admin.register(User)
class UserAdmin(ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(ModelAdmin):
    pass
