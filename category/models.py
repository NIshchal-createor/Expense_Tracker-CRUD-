from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.utils.text import slugify


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, validators=[MinLengthValidator(5), MaxLengthValidator(20)])
    slug = models.SlugField(null=False, blank=True, unique=True)

    def __str__(self):
        return f"{self.name}"
    
    def save(self):
        self.slug = slugify(self.name)
        super().save()
