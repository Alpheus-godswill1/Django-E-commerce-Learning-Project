from django.shortcuts import render
from .models import Item, OrderItem, Order

# Create your views here.
def item_list(request):
    content =  {'Items': Item.objects.all()}
    return render(request, "commercemaster/'f{'hello and welcome'}'", content)