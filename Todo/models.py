from django.db import models 
from django.utils import timezone 
from django.contrib.auth.models import User
# Create your models here.

class TodoModel(models.Model):
	usr = models.ForeignKey(User, on_delete = models.CASCADE, null = True) 
	title=models.CharField(max_length=100, null = True) 
	details=models.TextField(null = True) 
	date=models.DateTimeField(default=timezone.now, null = True) 

	def __str__(self): 
		return self.title 
