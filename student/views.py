from django.shortcuts import render
from student.models import students , Course
# Create your views here.

def student_view (request) : 
    all_students = students.objects.all() 
    context = {"students" : all_students}
    html_file = "student/all_student.html" 
    return render(request , html_file , context)



def courses_view (request) : 
    all_courses = Course.objects.all()
    context = {"course" : all_courses}
    return render (request , 'student/courses.html ', context)