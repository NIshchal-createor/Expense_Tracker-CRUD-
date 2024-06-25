from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.

class Expense(models.Model):
    description = models.TextField(validators=[MaxLengthValidator(255), MinLengthValidator(10)])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.amount}"
