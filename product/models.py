from django.db import models
from student.models import students
# Create your models here.

class task(models.Model) : 
    title = models.CharField(max_length = 256)
    done = models.BooleanField(default=False)
    category = models.CharField(max_length = 56)
    description = models.TextField() 
    # date = models.DateField()  
    student = models.ForeignKey(students , on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class Typecategory(models.Model) : 
    title = models.CharField(max_length=32)
    tasks = models.ManyToManyField(task)
    def __str__(self):
        return self.title