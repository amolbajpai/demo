from django.db import models

# Create your models here.
class ImpDatesModel(models.Model):
    name = models.CharField(max_length=50)
    occasion = models.CharField(max_length=50)
    date = models.DateField()
    remarks = models.CharField(max_length=50)