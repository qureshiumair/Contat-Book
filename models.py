from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=20)
    relationship=models.CharField(max_length=15)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=30)
    