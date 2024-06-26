from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['description', 'amount', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),  # Adjust rows as needed
            'category': forms.Select(attrs={'class': 'form-select'})  # Bootstrap form-select class
        }
