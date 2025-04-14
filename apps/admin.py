from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import User, SiteSettings, Question, Answer


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = 'username', 'first_name', 'last_name', 'email', 'name', 'is_active',
    list_editable = 'is_active',
    list_filter = 'is_active',


@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    list_display = 'region_to_region',


@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = 'text', 'created_at',
    list_filter = 'created_at',


@admin.register(Answer)
class AnswerAdmin(ModelAdmin):
    list_display = 'text', 'question', 'created_at',
    list_filter = 'created_at',

# from django.contrib import admin
# from django.contrib.admin import ModelAdmin
#
# from apps.models import User, Project, Task
#
#
# @admin.register(User)
# class UserAdmin(ModelAdmin):
#     list_display = 'username', 'role', 'user_type', 'created_at',
#     list_editable = 'role', 'user_type',
#     list_filter = 'role', 'user_type',
#
#
# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = "name", "manager", "manager", "display_team_members", "created_at",
#     list_editable = "manager",
#
#     def display_team_members(self, obj):
#         return ", ".join([user.username for user in obj.team_members.all()])
#
#     display_team_members.short_description = "Team Members"
#
#
# @admin.register(Task)
# class TaskAdmin(ModelAdmin):
#     list_display = 'project', 'title', 'assigned_to', 'status', 'created_at',
#     list_editable = 'status', 'assigned_to',
#     list_filter = 'title',
