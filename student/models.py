from django.db import models

# Create your models here.

class students (models.Model): 
    name = models.CharField (max_length=64) 
    score = models.IntegerField() 
    full_name = models.CharField (max_length=64)
    phone_number = models.CharField(max_length=13)
    def __str__(self):
        return self.full_name

class Course(models.Model) : 
    title = models.CharField(max_length=64)
    code = models.PositiveBigIntegerField()
    desc = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    students = models.ManyToManyField(students , related_name= "courses")
    def __str__(self):
        return self.title


class profile (models.Model) : 
    bio = models.TextField()
    avatar = models.CharField(max_length=128)
    students = models.OneToOneField(students , related_name= "profile" , on_delete= models.CASCADE)
    def __str__(self):
        return self.bio
    
