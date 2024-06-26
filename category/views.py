from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from category.forms import CategoryForm
from category.models import Category
from django.urls import reverse_lazy

# Create your views here.

class CreateCategory(CreateView):
    print("Entered Here")
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('category:list')


class ListCategory(ListView):
    model = Category
    template_name = 'category/list.html'
    context_object_name = 'categories'

class UpdateCategory(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/update.html'
    success_url = reverse_lazy("category:list")


class DeleteCategory(DeleteView):
    model = Category
    success_url = reverse_lazy('category:list')
