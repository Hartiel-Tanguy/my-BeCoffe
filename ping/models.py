from enum import unique
from django.db import models
from django.utils import timezone


# Create your models here.

class precence(models.Model):
    date = models.DateTimeField(null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    matin = models.TimeField(null=False)
    soir = models.TimeField(blank=True, null=True)

    class Meta:
        unique_together = ('date', 'user')

    def __str__(self):
        return f"{self.id} {self.user} {self.matin.strftime('%y-%m-%d %H:%M')} {self.soir}"