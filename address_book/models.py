from django.db import models
from django.core.validators import MinValueValidator
class Address(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 50)
    phone = models.IntegerField(validators=[MinValueValidator(1)])
    city = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    zipcode = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name
