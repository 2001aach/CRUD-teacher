from django.db import models

# Create your models here.

class teacher(models.Model):
    name=models.CharField(max_length=250)
    attendance=models.CharField(max_length=250)
    date=models.DateField()
