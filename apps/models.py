from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model, CharField, TextField, ForeignKey, CASCADE, DateTimeField, ManyToManyField
from django.db.models.fields import IntegerField


class User(AbstractUser):
    pass


class Project(Model):
    name = CharField(max_length=100, help_text='Project name: ')
    task = TextField(help_text='Write your task: ')
    created_at = DateTimeField(auto_now_add=True)
    member_of_project = IntegerField(default=0)
    date_line = CharField(max_length=100, help_text='Date line of your task (1 month): ')
    user = ForeignKey('apps.User', CASCADE, related_name='projects')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"Project name: {self.name}"


class Task(Model):
    name = CharField(max_length=100, help_text='Task name: ')
    user = ManyToManyField('apps.User')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"task name: {self.name}"
