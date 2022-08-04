from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.core.models import Category, Product, Review
from .forms import UserRegisterForm, ProductForm, ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterForm(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


def base(request):
    context = {'categories': Category.objects.all()}
    return render(request, 'base.html', context)


def about(request):
    context = {'categories': Category.objects.all()}
    return render(request, 'about.html', context)


def product(request):
    context = {
        'products': Product.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'product.html', context)


def products_in_category(request, pk):
    category = Category.objects.get(pk=pk)
    context = {
        'category': Category.objects.get(pk=pk),
        'products_in_category': Product.objects.filter(category=category),
        'categories': Category.objects.all(),
    }
    return render(request, 'productsInCategory.html', context)


class CreateProductView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "createProduct.html"
    form_class = ProductForm


class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = "createReview.html"
    form_class = ReviewForm
