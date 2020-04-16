from django.urls import path

from .views import *

urlpatterns = [
    path('', startpage_response, name='index'),
    path('list', productlist_response, name='product_list'),
    path('productbye', productbye_response, name='product_bye'),
    path('shop', shop_response, name='shop'),
    path('aboutus', abouteus_respose, name='about_us' ),
    path('linux', linux_response, name='linux')
]