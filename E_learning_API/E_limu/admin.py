from django.contrib import admin
from .models import Subject, Course


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Subject, SubjectAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('subject', 'title', 'slug', 'overview','created')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Course, CourseAdmin)











 
