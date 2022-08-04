from django.forms import ModelForm
from .models import User, Product, Review
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email -- ",
                "class": ""
            }
        ))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Этот email уже занят")

        return email


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'title', 'description', 'rating']
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
        }


