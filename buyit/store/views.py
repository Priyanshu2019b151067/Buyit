from django.shortcuts import render
from .models import Product
def all_product(request):
    products = Product.objects.all()
    return render(request,'store/all.html',{'products':products})