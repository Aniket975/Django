from django.shortcuts import render
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist


def say_hello(request):        
    return render(request, 'hello.html', {'name': 'Aniket',})
