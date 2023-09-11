from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Person(models.Model):
    name = models.CharField(unique=True, max_length=255)
    
    def validate_name(value):
        if not isinstance(value):
            return ValidationError(_("Name must be string."))
    
    def __str__(self):
        return self.name
