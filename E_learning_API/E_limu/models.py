from django.db import models
from django.conf import settings
from E_learning_API.profiles.models import Student, Instructor


class TimestampedModel(models.Model):
    """
    Base class with `created` and `modified` fields.
    """
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True



class Subject(TimestampedModel, models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    def __str__(self):
        return self.title


class Course(TimestampedModel, models.Model):
    instructor = models.ForeignKey(Instructor, related_name='courses_created', on_delete=models.CASCADE,)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
   
    

    def __str__(self):
        return self.title


class Quiz(TimestampedModel, models.Model):
    FORM_CHOICES = ( 
    ("1", "1"), 
    ("2", "2"), 
    ("3", "3"), 
    ("4", "4"), )
    level = models.ForeignKey(choices=FORM_CHOICES, default='1')
    subject = models.ForeignKey(Subject, related_name='quizzes', on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    
    def __str__(self):
        return self.title


class Badge(TimestampedModel, models.Model):
    Quiz = models.OneToOneField(Quiz, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
    

class Question(TimestampedModel, models.Model):
    question = models.CharField(max_length=50, unique=True)

class Choice(TimestampedModel, models.Model):
    question = models.ForeignKey("Question", related_name="choices")
    choice = models.CharField("Choice", max_length=50)
    position = models.IntegerField("position")

    class Meta:
        unique_together = [
            # no duplicated choice per question
            ("question", "choice"), 
            # no duplicated position per question 
            ("question", "position") 
        ]
        ordering = ("position",)

