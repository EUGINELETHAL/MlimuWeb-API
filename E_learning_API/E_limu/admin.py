from django.contrib import admin
from .models import Subject, Course, Choice, Question, Quiz


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Subject, SubjectAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('subject', 'title', 'slug', 'overview', 'created')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Course, CourseAdmin)


class ChoiceInline(admin.StackedInline):
    model = Choice
    fieldsets = [
        (None,               {'fields': ['choice']}),
        (None,               {'fields': ['is_correct']}),
         (None,               {'fields': ['position']}),
       
    ]
class QuizAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['slug']}),
        (None,               {'fields': ['pass_mark']}),
        (None,               {'fields': ['single_attempt']}),
        (None,               {'fields': ['level']}),
        
    ]


admin.site.register(Quiz, QuizAdmin)


class QuestionAdmin(admin.ModelAdmin):
    
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)














 
