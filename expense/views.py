from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from expense.models import Expense
from expense.form import ExpenseForm
from category.models import Category
from django.views import View
from django.shortcuts import redirect, render


# Create your views here.

class CreateExpense(View):
    def get(self, request, slug):
        try:   
            category = Category.objects.get(slug=slug)
            print(category)
            return render(request, template_name='expense/create.html', context={'category': category})
        except Exception as e:
            return render(request, template_name='expense/create.html', context={'error': e})
        
    def post(self, request, slug):
        try:
            category = Category.objects.get(slug=slug)
            expenses = Expense(
                description = request.POST['description'],
                amount = float(request.POST['amount']),
                category_id = category.id
            )
            expenses.save()
            return redirect('expenses:list', slug=category.slug)
        except Exception as e:
            return render(request, template_name="expense/create.html", context= {'error': e, 'category': category})
            


class ListExpenses(View):
    def get(self, request, slug):
        try:
            category = Category.objects.get(slug=slug)
            expenses = Expense.objects.filter(category_id=category.id)
            print(type(expenses))
            return render(request, template_name='expense/list.html', context={'category': category, 'expenses': expenses})
        except Exception as e:
            print(e)
            return render(request, template_name="expense/list.html", context={'error': e})


class DeleteExpenses(View):
    def post(self, request, pk):
        try:
            expense = Expense.objects.get(pk=pk)
            category = Category.objects.get(pk=expense.category_id)
            expense.delete()
            return redirect('expenses:list', slug = category.slug)
        except Exception as e:
            redirect('expenses:list', slug = category.slug)

class UpdateCategory(View):
    def get(self, request, pk):
        try:
            expense = Expense.objects.get(pk=pk)
            category = Category.objects.get(pk=expense.category_id)
            return render(request, 'expense/update.html', context={'expense': expense, 'category_slug': category.slug})
        except Exception as e:
            return redirect('expenses:list', slug = category.slug)
    def post(self, request, pk):
        try:
            expense = Expense.objects.get(pk=pk)
            category = Category.objects.get(pk=expense.category_id)
            expense.description = request.POST['description']
            expense.amount = float(request.POST['amount']) 
            expense.save()
            return redirect('expenses:list', slug = category.slug)
        except Exception as e:
            return redirect('expenses:update', slug = category.slug)

            
