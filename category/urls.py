from category.views import CreateCategory, ListCategory, UpdateCategory, DeleteCategory
from django.urls import path

app_name = 'category'

urlpatterns = [
    path('',  ListCategory.as_view(), name = 'list'),
    path("add", CreateCategory.as_view(), name='add'),
    path('update/<slug:slug>', UpdateCategory.as_view(), name='update'),
    path('delete/<slug:slug>', DeleteCategory.as_view(), name='delete')
]
