from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('Subjects', views.SubjectList.as_view()),
    path('Subjects/<int:pk>/', views.SubjectDetail.as_view()),
    path('Subjects/Courses', views.CourseList.as_view()),
    path('Subjects/Courses/<int:pk>/', views.course_detail)

]


urlpatterns = format_suffix_patterns(urlpatterns)