from django.forms import ModelForm
from student.models import students
from student.models import Course

class StudentForm(ModelForm): 
    class Meta : 
        model = students 
        fields = ['full_name', 'user']

  

class CourseStudentForm(ModelForm) : 
    class Meta : 
        model = Course
        fields = ["title" , "desc"]
