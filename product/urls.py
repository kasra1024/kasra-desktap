from django.urls import path 
from product.views import home

urlpatterns = [path('home/',home)]