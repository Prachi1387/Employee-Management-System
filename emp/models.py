from django.db import models
from unittest.util import _MAX_LENGTH
from email.policy import default

class Emp(models.Model):
    emp_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=200)

    def __str__(self):
        return self.name
# Create your models here.

