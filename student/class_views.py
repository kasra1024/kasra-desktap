from django.views import View
from student.models import *
from student.forms import StudentForm
from django.shortcuts import render

class AllStudentsView (View) : 
    html_file = "student/all_student.html"

    def get (self , request) : 
        form = StudentForm
        all_students = students.objects.all() 
        context = {"studentss" : all_students , "form" : form} 
        return render (request , self.html_file , context)