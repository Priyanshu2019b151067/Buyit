from django.urls import path
from .views import (all_product)
app_name = 'store'
urlpatterns = [
    path('',all_product,name='all_product'),
]
