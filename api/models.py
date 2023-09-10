from django.db import models

class Person(models.Model):
    name = models.CharField(unique=True, max_length=255)
