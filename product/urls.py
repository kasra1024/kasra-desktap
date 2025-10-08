from django.urls import path 
from product.views import home , task_new

urlpatterns = [path('home/',home) ,
               path ('home2/' , task_new) 
               ]
