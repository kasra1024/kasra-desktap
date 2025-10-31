from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class students (models.Model):
    user = models.OneToOneField(User , related_name= 'student' , on_delete= models.CASCADE ) 
    full_name = models.CharField (max_length=64)
    score = models.IntegerField() 

   
    def __str__(self):
        return self.full_name
    


# ------------------------------------------------------------
class Course(models.Model) : 
    title = models.CharField(max_length=64)
    code = models.PositiveBigIntegerField()
    desc = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    students = models.ManyToManyField(students , related_name= "courses")
    def __str__(self):
        return self.title
# --------------------------------------------------------------




class Teacher (models.Model) : 
    user = models.OneToOneField(User , related_name="teacher", on_delete= models.CASCADE)
    fullname = models.CharField (max_length=64)
    score = models.IntegerField() 
    def __str__(self):
        return self.fullname










class profile (models.Model) : 
    bio = models.TextField()
    avatar = models.CharField(max_length=128)
    phone_number =models.IntegerField(max_length=13) 
    img = models.ImageField(upload_to="images/%Y/%m/" , null=True)
    file = models.FileField(upload_to="files/%Y/%m/" , null=True)
    students = models.OneToOneField(students , related_name= "profile" , on_delete= models.CASCADE , null=True , blank=True)
    Teacher = models.OneToOneField(Teacher , related_name= "profile" , on_delete= models.CASCADE , null=True , blank=True)
    def __str__(self):
        return self.bio







    