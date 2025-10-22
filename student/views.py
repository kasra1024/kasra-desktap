from django.shortcuts import render , redirect
from student.models import students , Course
from student.forms import StudentForm
# Create your views here.


def student_view (request) : 
    form = StudentForm()
    html_file = "student/all_student.html" 
    if request.method == 'GET' : 

        all_students = students.objects.all() 
        context = {"students" : all_students , "form": form}
        
        return render(request , html_file , context)
    
    elif request.method == 'POST' : 
        data = request.POST
        fullname1 = data['full_name'] 
        username1 = data['name'] 
        phone1 = data['phone_unmber'] 
        students.objects.create(full_name = fullname1 , name = username1 , phone_number = phone1 , score = 0)
        return render (request , html_file , {"form" : form})














# ---------------------------------------------------------------------
def courses_view (request) : 
    all_courses = Course.objects.all()
    context = {"course" : all_courses}
    return render (request , 'student/courses.html ', context)