from django.db import models

# Create your models here.
class position(models.Model):
	title=models.CharField(max_length=100)

	def __str__(self):
		return self.title

class Employee(models.Model):
	fullname=models.CharField(max_length=200)
	empcode=models.CharField(max_length=3)
	mobile=models.CharField(max_length=10)
	position=models.ForeignKey(position,on_delete=models.CASCADE)