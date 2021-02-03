from django.db import models
from E_learning_API import settings


class Instructor(models.Model):
    instructor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    slug = models.SlugField(max_length=200, unique=True)
    bio = models.TextField('bio', default='', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):  
        return self.instructor.username


class Student(models.Model):
    student = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    slug = models.SlugField(max_length=200, unique=True)
    bio = models.TextField('bio', default='', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):  
        return self.student.username