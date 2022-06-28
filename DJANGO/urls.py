from django.urls import path

from reachbuy.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='reachbuy'),
]
