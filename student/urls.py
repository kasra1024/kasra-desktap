from django.urls import path
from student.views import student_view , courses_view

urlpatterns = [
    path ('all_student/' , student_view) ,
    path ('courese/' , courses_view)
]