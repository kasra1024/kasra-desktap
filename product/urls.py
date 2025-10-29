from django.urls import path 
from product.views import *

app_name = "product"


urlpatterns = [path('home/',home) ,
               path ('home2/' , task_new) ,
               path ('home3/<int:st_id>/' , task_student , name="home later") , 
               ]
