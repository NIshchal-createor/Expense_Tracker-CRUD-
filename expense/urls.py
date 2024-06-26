from expense.views import CreateExpense, ListExpenses, DeleteExpenses, UpdateCategory
from django.urls import path

app_name = 'expenses'

urlpatterns = [
    path('<slug:slug>',  ListExpenses.as_view(), name = 'list'),
    path("add/<slug:slug>", CreateExpense.as_view(), name='add'),
    path("delete/<int:pk>", DeleteExpenses.as_view(), name='delete'),
    path('update/<int:pk>', UpdateCategory.as_view(), name='update'),
    # path('delete/<slug:slug>', DeleteCategory.as_view(), name='delete')
]
