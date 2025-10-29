from django.urls import path 
from account.views import RegisterView 

app_name = "account" 

urlpatterns = [
    path ("user_register/" , RegisterView.as_view() , name="user_register")
]