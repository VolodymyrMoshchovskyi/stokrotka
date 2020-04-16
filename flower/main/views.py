from django.shortcuts import render

from .models import *

# Create your views here.
def startpage_response(request):
    return render(request, 'index.html')

def productlist_response(request):
    all_product = Product.objects.all().order_by('title')
    return render(request, 'product-list.html', { 'products': all_product})

def productbye_response(request):
    return render(request, 'product-bye.html')


def shop_response(request):
    return render(request, 'index.html')


def abouteus_respose(request):
    return render(request, 'about-us.html')


def linux_response(request):
    return render(request, 'linux.html')


