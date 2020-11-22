from django.db import models
from E_learning_API import settings
from django.db.models.signals import post_save
from E_learning_API.authentication.models import User



class Instructor(models.Model):
    instructor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    slug = models.SlugField(max_length=200, unique=True)
    bio = models.TextField('bio', default='', null=True, blank=True)
    school = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):  
        return self.instructor.username

# def create_profile(sender, **kwargs):
#     user = kwargs["instance"]
#     if kwargs["created"]:
#         user_profile = Instructor(user=user)
#         user_profile.save()
# post_save.connect(create_profile, sender=User)

class Student(models.Model):
    student = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='user')
    slug = models.SlugField(max_length=200, unique=True)
    bio = models.TextField('bio', default='', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):  
        return self.instructor.username