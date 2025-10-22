from django.forms import ModelForm
from student.models import students

class StudentForm(ModelForm): 
    class Meta : 
        model = students 
        fields = ['full_name', 'name', 'phone_number']

