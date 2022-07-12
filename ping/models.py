from enum import unique
from django.db import models
from django.utils import timezone
from compte.models import users


# Create your models here.

class presence(models.Model):
    date = models.DateField(null=True)
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    matin = models.TimeField(null=False)
    soir = models.TimeField(blank=True, null=True)

    class Meta:
        unique_together = ('date', 'user')