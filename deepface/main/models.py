from django.contrib.postgres.fields import ArrayField
from django.db import models


class Document(models.Model):
    client_id = models.CharField(max_length=200)
    coffee_type = models.CharField(max_length=100)
    file = models.ImageField()
    age = models.CharField(max_length=150)
    ethnicity = models.CharField(max_length=150)
    gender = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    pixels = ArrayField(models.IntegerField())
