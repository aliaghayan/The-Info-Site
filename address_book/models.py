from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
class Address(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 50)
    phone = models.BigIntegerField(default=1,validators=[MaxValueValidator(9999999999999999),MinValueValidator(0)])
    company = models.CharField(max_length = 200)
    address = models.CharField(max_length = 1000)
    city = models.CharField(max_length = 35)
    state = models.CharField(max_length = 50)
    zipcode = models.BigIntegerField(default=1,validators=[MaxValueValidator(99999999999999999),MinValueValidator(0)])

    def __str__(self):
        return self.name
