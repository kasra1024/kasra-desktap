from django.urls import path
from student.views import student_view , courses_view , CreateStudent , CourseStudentForm , course_list
from student.class_views import AllStudentsView


app_name = "student"

urlpatterns = [
    path ('all_student/' , student_view) ,
    path ('courese/' , courses_view , name = "student_list") ,
    path ("all_students_new/" , AllStudentsView.as_view()) ,
    path ("student_create/" , CreateStudent.as_view(), name= "student_create_new"), 
    path ("course_student_form/" , CourseStudentForm , name="course_add") ,
    path ("course_list/" , course_list , name="course_list_new") ,
    ] 