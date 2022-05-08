from django.contrib.postgres.fields import ArrayField
from django.db import models


class Document(models.Model):
    file = models.ImageField()
    age = models.CharField(max_length=150)
    ethnicity = models.CharField(max_length=150)
    gender = models.CharField(max_length=10)
    pixels = ArrayField(models.IntegerField())
