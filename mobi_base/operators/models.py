from django.db import models
from django_countries.fields import CountryField


class Operator(models.Model):
    operator_name = models.CharField(max_length=64)
    apn = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    iccid = models.CharField(max_length=100)
    esim_status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.operator_name}"