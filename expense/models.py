from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from category.models import Category

class Expense(models.Model):
    description = models.TextField(validators=[MaxLengthValidator(255), MinLengthValidator(10)])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)  # Assuming Category ID 1 exists
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.description} - {self.amount}"
    
