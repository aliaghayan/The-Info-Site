from django.db import models
from django.core.validators import MinValueValidator
class Address(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 50)
    phone = models.CharField(max_length=11)
    company = models.CharField(max_length = 200)
    address = models.CharField(max_length = 1000)
    city = models.CharField(max_length = 35)
    state = models.CharField(max_length = 50)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return self.name
