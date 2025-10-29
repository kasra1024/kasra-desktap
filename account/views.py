from django.shortcuts import render , redirect
from django.views import View 
from django.contrib.auth.models import User
from account.forms import UserRegisterForm

# Create your views here.

 
class RegisterView(View) : 

    form = UserRegisterForm() 
    template = "account/Register.html"

    def get (self , request) : 
        return render (request , self.template , {"form" : self.form})
    
    def post (self , request) : 
        st_form = UserRegisterForm(request.POST)
        if st_form.is_valid(): 
            new_user = st_form.save()
            if new_user : 
                return None
        
        return render (request , self.template , {"form" : self.form , "message" : "username is valid"})  
