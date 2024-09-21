from django.shortcuts import render
from store.models import Product

# Create your views here.


def say_hello(request):
    query_set = Product._default_manager.all()

    for product in query_set:
        print(product)

    return render(request, "hello.html", {"name": "Lokyra"})
