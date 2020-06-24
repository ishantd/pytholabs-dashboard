from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Module(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    allow_comments = models.BooleanField(null=False, default=True)
    timestamp = models.DateField(default=timezone.now, null=False)

class Topic(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    allow_comments = models.BooleanField(null=False, default=True)
    timestamp = models.DateField(default=timezone.now, null=False)

class Subtopic(models.Model):
    subtitle = models.CharField(max_length=150, null=True, blank=True)
    title = models.ForeignKey(Topic, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    allow_comments = models.BooleanField(null=False, default=True)
    timestamp = models.DateField(default=timezone.now, null=False)
