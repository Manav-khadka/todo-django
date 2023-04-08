from django.db import models

# Create your models here.
class Task(models.Model):
    taskTitle=models.CharField(max_length=30)
    taskDsc=models.TextField()
    time = models.DateTimeField(auto_now_add=True)
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)