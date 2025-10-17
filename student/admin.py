from django.contrib import admin
from student.models import students , Course , profile
# Register your models here.
admin.site.register(students)
admin.site.register(Course)
admin.site.register(profile)