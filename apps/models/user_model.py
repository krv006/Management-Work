from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db.models import EmailField, BooleanField

from apps.models.user_model_config import CustomUserManager


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = EmailField(unique=True)
    name = CharField(max_length=255)
    is_active = BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        app_label = 'apps'
