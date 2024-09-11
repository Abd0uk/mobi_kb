from django.db import models
from django_countries.fields import CountryField


class Operator(models.Model):
    operator_name = models.CharField(max_length=64)
    provider_name = models.CharField(max_length=124, default='n/a')
    apn = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    iccid = models.CharField(max_length=100)
    esim_status = models.CharField(max_length=100)

    check_usage = models.CharField(max_length=200, default='n/a')
    topup_eligibility = models.CharField(max_length=500, default='n/a')

    kyc = models.CharField(max_length=500, default='n/a')

    activation = models.CharField(max_length=1000, default='n/a')
    replacement = models.CharField(max_length=1000, default='n/a')
    cancellation = models.CharField(max_length=1000, default='n/a')


    def __str__(self):
        return f"{self.operator_name}"