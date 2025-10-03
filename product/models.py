from django.db import models

# Create your models here.

class task(models.Model) : 
    title = models.CharField(max_length = 256)
    done = models.BooleanField(default=False)
    category = models.CharField(max_length = 56)
    description = models.TextField() 
    date = models.DateField() 