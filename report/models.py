from django.db import models
from datetime import datetime

# Create your models here.
class CabProcessing(models.Model):
    requestid = models.PositiveIntegerField()
    name=models.CharField(max_length=250)
    servicetype=models.CharField(max_length=250)
    source=models.CharField(max_length=250,default="ENSIM INDIA PVT.LTD")
    destnation=models.CharField(max_length=250)
    Date=models.DateField()
    Pickuptime=models.TimeField()
    issuedto=models.CharField(max_length=250)
    Empid=models.PositiveIntegerField()
    Drivername=models.CharField(max_length=250)
    status=models.CharField(max_length=250)
    fare=models.PositiveIntegerField()
    location=models.CharField(max_length=250)

def __str__(self):
    return self.requestid