from django.shortcuts import render
# from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product


def say_hello(request):
    # query_set = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    # query_set = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # query_set = Product.objects.filter(Q(inventory__lt=10) | ~Q(unit_price__lt=20))
    # query_set = Product.objects.filter(inventory = F('unit_price'))
    query_set = Product.objects.filter(inventory = F('collection__id'))

    return render(request, 'hello.html', {'name': 'Aniket', 'products': list(query_set)})
