from datetime import timedelta
from django.db import models
from django.conf import settings
import itertools  
from django.utils.translation import ugettext as _
from django.utils.text import slugify 
from E_learning_API.profiles.models import Student, Instructor
from django.core.validators import MaxValueValidator, validate_comma_separated_integer_list


class TimestampedModel(models.Model):
    """
    Base class with `created` and `modified` fields.
    """
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class Subject(TimestampedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    def __str__(self):
        return self.title


class Course(TimestampedModel):
    instructor = models.ForeignKey(Instructor, related_name='courses_created',
                                   on_delete=models.CASCADE,)
    subject = models.ForeignKey(Subject, related_name='courses', 
                                on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
   
    

    def __str__(self):
        return self.title


class Quiz(TimestampedModel):
    FORM_CHOICES = ( 
    ("1", "1"), 
    ("2", "2"), 
    ("3", "3"), 
    ("4", "4"), )
    level = models.CharField(choices=FORM_CHOICES, max_length=20)
    # subject = models.ForeignKey(Subject, related_name='quizzes', 
    #                             on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    single_attempt = models.BooleanField(blank=False, default=False, 
                                         help_text=(" only one attempt"),
                                         verbose_name=("Single Attempt"))
    pass_mark = models.SmallIntegerField(blank=True, default=0,
                                         verbose_name=("Pass Mark"), 
                                         help_text=("Score required to pass exam."),
                                         validators=[MaxValueValidator(100)])
    success_text = models.TextField(
        blank=True, help_text=_("Displayed if user passes."),default="Hurray you have passed",
        verbose_name=_("Success Text"))

    fail_text = models.TextField(
        verbose_name=_("Fail Text"),default="Hurray you have failed",
        blank=True, help_text=_("Displayed if user fails."))

    draft = models.BooleanField(
        blank=True, default=False,
        verbose_name=_("Draft"))

    duration = models.DurationField(default=timedelta(minutes=40))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Quiz, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
   

class Badge(TimestampedModel):
    Quiz = models.OneToOneField(Quiz,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
    

class Question(TimestampedModel):
    quiz = models.ForeignKey("Quiz", related_name="questions",
                             on_delete=models.CASCADE)
    question_text = models.CharField(max_length=1024, unique=True)
    hint = models.CharField(max_length=1024, blank=True)

    # @property
    # def get_choice_types(self):
    #     choice_id=self.choices.values_list('id', flat=True)
    #     choice_letters = ['a', 'b', 'c','d']
    #     for (a, b) in zip(choice_id, choice_letters): 
    #                     return self.choice_types.append(("a",b))
    #     return self.choice_types
    #     print(self.choice_types)

    # def __str__(self):
    #     return  self.question_text

    
    


class Choice(TimestampedModel):
    
    # def choice_types():
    #     for i in [1, 2, 3, 4]:
    #         return i

    question = models.ForeignKey("Question", related_name="choices", 
                                 on_delete=models.CASCADE)
    # position = models.CharField(choices=choice_position, max_length=50)                             
    choice = models.CharField(max_length=100)
    choice_types=models.CharField( max_length=100)
    is_correct=models.BooleanField(default=False)


    # def save(self, *args, **kwargs):
    #     choice_id=self.objects.values_list('id', flat=True)
       

        
    #     self.choice_types = slugify(self.headline)
    #     super(Article, self).save(*args, **kwargs)

   
    def get_choice_types(self,question_id):
        question=Question.objects.get(id=question_id)
        choice_id=question.choices.values_list('id', flat=True)
        choice_letters = ['a', 'b', 'c','d']
        for (a, b) in zip(choice_id, choice_letters): 
                print((a,b)) 
       
        
       
        
       
        

   

    def __str__(self):
        return self.choice

   
    
@staticmethod
def funcname(parameter_list):
    pass


    # class Meta:
    #     unique_together = [
    #         # no duplicated choice per question
    #         ("question", "choice"), 
    #         # no duplicated position per question 
    #         ("question", "position") 
    #     ]
    #     ordering = ("position",)

    # def __str__(self):
    #     return '%s: %s' % (self.position, self.choice)


    def is_correct_choice(self):
        return self.is_correct


class StudentAnswer(TimestampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_answers')
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='student_answers')
