from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from webapp.forms import CategoryForm
from webapp.models import Category


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'category/category_list.html'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_create.html'


class CategoryUpdateView(UpdateView):
    model = Category
    context_object_name = 'category'
    form_class = CategoryForm
    template_name = 'category/category_update.html'


class CategoryDeleteView(DeleteView):
    model = Category

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.products.count() == 0:
            self.object.delete()
        return redirect('category-list')

