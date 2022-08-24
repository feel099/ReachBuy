from django.urls import path
from apps.core import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.RegisterForm.as_view(), name='register'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('', views.base, name='base'),
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('productsInCategory/product_page/<int:pk>', views.product_page, name='product_page'),
    path('productsInCategory/<int:pk>', views.products_in_category, name='productsInCategory'),
    path('createProduct/', views.CreateProductView.as_view(), name='createProduct'),
    path('createReview/', views.CreateReviewView.as_view(), name='createReview'),
]
