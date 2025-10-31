from django.shortcuts import render , redirect
from django.views import View 
from django.contrib.auth.models import User
from account.forms import UserRegisterForm , UserLoginFrom 

from django.contrib.auth import authenticate , login , logout

# Create your views here.

# hoviat

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


# ====================================================================================================================================================================
# login

class LoginView(View) : 
    form = UserLoginFrom ()
    html = "account/login.html"

    def get (self , request) : 
        return render (request , self.html , {"form" : self.form})
    


    def post (self , request) : 
        form =UserLoginFrom(request.POST)
        # if form.is_valid() :
        user = authenticate(username = request.POST["username"] ,password = request.POST["password"])
        
        if user and user.is_authenticated : 
            login(request , user) 
            return redirect ("student:add_course")
        return render (request , self.html , {"form" : self.form , "message" : "username and password is valid"})
    


# ====================================================================================================================================================================
# logout

class LogoutView(View) : 
    def get (self , request) : 
        if request.user.is_authenticated : 
            logout(request)
        return redirect ("account:user_login")
    
# ----------------------------------------------------------------------
# delet

class DeleteView (View) : 
    def get (self , request) : 
        if request.user.is_authenticated :
            try : 
                user= User.objects.get(id=request.user.id) 
                user.delete()
                return redirect("product:home")
            except :
                return redirect("studet:add_course")