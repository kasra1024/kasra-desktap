from django.urls import path 
from account.views import *

app_name = "account" 

urlpatterns = [
    path ("user_register/" , RegisterView.as_view() , name="user_register") ,
    path ("user_login/" , LoginView.as_view() , name= "user_login") ,
    path ("user_logout/" , LogoutView.as_view() , name= "user_logout") ,
    path ("user_delete/" , DeleteView.as_view() , name= "user_delete") ,
]