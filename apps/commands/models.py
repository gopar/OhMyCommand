from django.db import models
from django.conf import settings


class Command(models.Model):
    OS_CHOICES = (
        ('A', 'Any'),
        ('L', 'Linux'),
        ('M', 'Mac'),
        ('W', 'Windows'),
        ('O', 'Other'))

    command = models.TextField(
        max_length=300, help_text='Enter command to remember')
    os = models.CharField(max_length=1, choices=OS_CHOICES, blank=True)
    version = models.CharField(
        max_length=20, help_text='Version command works on', blank=True)
    note = models.TextField(
        max_length=500, help_text='Any information on command', blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.command[:20]
