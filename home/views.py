
from .models import Product

from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request,'index.html')
def task(request):
    return render(request,'task.html')


def product_list(request):
    products = Product.objects.all()
    data = [{'name': product.name, 'description': product.description, 'price': product.price, 'created_at': product.created_at} for product in products]
    return JsonResponse(data, safe=False)

