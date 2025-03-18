from django.contrib.auth.models import AbstractUser
from django.db import models


# USER ROLES
class UserRole(models.TextChoices):
    SUPER_ADMIN = "super_admin", "Super Admin"
    PROJECT_MANAGER = "project_manager", "Project Manager"
    USER = "user", "User"


# USER TYPES
class UserType(models.TextChoices):
    ANALYST = "analyst", "Analyst"
    ENGINEER = "engineer", "Engineer"


# CUSTOM USER MODEL
class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.USER,
        help_text="Foydalanuvchi roli: Super Admin, Project Manager yoki Oddiy User"
    )
    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.ENGINEER,
        help_text="Foydalanuvchi turi: Analyst yoki Engineer"
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


# PROJECT MODEL
class Project(models.Model):
    name = models.CharField(
        max_length=255,
        help_text="Loyihaning nomi"
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Loyihaning qisqacha tavsifi"
    )
    manager = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="managed_projects",
        help_text="Loyihaga mas'ul bo'lgan Project Manager"
    )
    team_members = models.ManyToManyField(
        User,
        related_name="projects",
        help_text="Loyiha jamoasi a'zolari"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Loyiha yaratilgan sana"
    )

    def __str__(self):
        return f"{self.name}"


# TASK STATUS
class TaskStatus(models.TextChoices):
    PENDING = "pending", "Pending"
    IN_PROGRESS = "in_progress", "In Progress"
    DONE = "done", "Done"


# TASK MODEL
class Task(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks",
        help_text="Qaysi loyihaga tegishli ekanligi"
    )
    title = models.CharField(
        max_length=255,
        help_text="Topshiriq (task) nomi"
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Topshiriqning batafsil tavsifi"
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks",
        help_text="Ushbu topshiriq kimga biriktirilgan"
    )
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING,
        help_text="Topshiriq holati: Pending, In Progress yoki Done"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Topshiriq yaratilgan sana"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Oxirgi marta yangilangan vaqt"
    )

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
