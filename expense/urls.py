from expense.views import CreateExpense, ListExpenses
from django.urls import path

app_name = 'expenses'

urlpatterns = [
    path('<slug:slug>',  ListExpenses.as_view(), name = 'list'),
    path("add/<slug:slug>", CreateExpense.as_view(), name='add'),
    # path('update/<slug:slug>', UpdateCategory.as_view(), name='update'),
    # path('delete/<slug:slug>', DeleteCategory.as_view(), name='delete')
]
