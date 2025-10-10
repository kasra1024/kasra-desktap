from django.db import models

# Create your models here.

class students (models.Model): 
    name = models.CharField (max_length=64) 
    score = models.IntegerField(max_length=64) 
    full_name = models.CharField (max_length=64)
    def __str__(self):
        return self.full_name