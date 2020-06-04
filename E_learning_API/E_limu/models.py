from django.db import models
from django.conf import settings
from E_learning_API.profiles.models import Student, Instructor






class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    def __str__(self):
        return self.title


class Course(models.Model):
    instructor = models.ForeignKey(Instructor, related_name='courses_created', on_delete=models.CASCADE,)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE,)
    students = models.ManyToManyField(Student)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title



