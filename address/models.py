from django.db import models

# Create your models here.
class Address(models.Model):
    fullname = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, default='')
    email = models.CharField(max_length=255, blank=True, default='')
    coutrycode = models.CharField(max_length=4, blank=True, default='')
    number = models.CharField(max_length=255, blank=True, default='')
    street = models.CharField(max_length=255)
    area = models.CharField(max_length=255, blank=True, default='')
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip  = models.CharField(max_length=12)
    fax = models.CharField(max_length=255, blank=True, default='')
    website = models.CharField(max_length=255, blank=True, default='')
    author = models.ForeignKey("users.user", on_delete=models.CASCADE, default=None)
