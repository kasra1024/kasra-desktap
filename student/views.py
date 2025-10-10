from django.shortcuts import render
from student.models import students
# Create your views here.

def student_view (request) : 
    all_students = students.objects.all() 
    context = {"students" : all_students}
    html_file = "student/all_student.html" 
    return render(request , html_file , context)
