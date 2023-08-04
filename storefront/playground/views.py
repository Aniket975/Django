from django.shortcuts import render
# from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import OrderItem


def say_hello(request):
    query_set = OrderItem.objects.filter(product__collection__id=3)

    return render(request, 'hello.html', {'name': 'Aniket', 'products': list(query_set)})
