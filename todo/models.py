from enum import unique
from django.db import models
from django.utils import timezone
from compte.models import users

class Todo(models.Model):
	user = models.ForeignKey(users, on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	details=models.TextField()
	date=models.DateField(default=timezone.now, unique=True)

	def __str__(self):
		return self.title
