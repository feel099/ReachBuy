from django.urls import path
from .views import base, about

urlpatterns = [
    path('', base, name='reachbuy'),
    path('about/', about, name='about'),
]
