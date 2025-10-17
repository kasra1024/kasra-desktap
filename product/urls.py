from django.urls import path 
from product.views import *

urlpatterns = [path('home/',home) ,
               path ('home2/' , task_new) ,
               path ('home3/<int:st_id>/' , task_student) , 
               ]
