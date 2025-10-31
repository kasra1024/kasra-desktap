from django.db.models.signals import post_save 
from django.dispatch import receiver
from student.models import students , profile

@receiver(post_save , sender = students)
def create_porfile(sender , instance , created , **kwargs) : 
    """ this function is create profile for students"""
    if created : 
        profile.objects.create(
            bio = f"{instance.full_name} bio" , student = instance
        )