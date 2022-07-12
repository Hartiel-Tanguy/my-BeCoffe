from enum import unique
from django.db import models
from django.utils import timezone
from compte.models import users


# Create your models here.

class presence(models.Model):
    date = models.DateTimeField(null=True)
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    matin = models.TimeField(null=False)
    soir = models.TimeField(blank=True, null=True)

    class Meta:
        unique_together = ('date', 'user')

#    def __str__(self):
 #       return f"{self.id} {self.user} {self.matin.strftime('%y-%m-%d %H:%M')} {self.soir}"