from django.urls import path

from .views import item_list

urlpatterns = [
    path('product/', item_list, name='product')
]