from django.shortcuts import render
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist


def say_hello(request):
    query_set = Product.objects.get(pk=0)
    return render(request, 'hello.html', {'name': 'Aniket', 'products':str(query_set)})
