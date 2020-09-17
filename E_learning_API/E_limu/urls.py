from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'E_learning_API.E_limu'

urlpatterns = [
    path('Subjects', views.SubjectList.as_view()),
    path('Subjects/<int:pk>/', views.SubjectDetail.as_view()),
    path('Subjects/Courses', views.CourseList.as_view()),
    path('Subjects/Courses/<int:pk>/', views.course_detail),
    path('questions', views.QuestionList.as_view(), name='questionlist'),
    path('quiz', views.Quizlist.as_view(), name='quiz-list'),
    path('quiz/<int:pk>/', views.QuizDetail.as_view()),
    path('question/<int:pk>/', views.QuestionDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
