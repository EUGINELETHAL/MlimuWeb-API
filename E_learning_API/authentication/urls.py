from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

  0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000urlpatterns = format_suffix_patterns(urlpatterns)urlpatterns = format_suffix_patterns(urlpatterns)urlpatterns = format_suffix_patterns(urlpatterns)urlpatterns = format_suffix_patterns(urlpatterns)urlpatterns = format_suffix_patterns(urlpatterns)urlpatterns = format_suffix_patterns(urlpatterns)urlpatterns = format_suffix_patterns(urlpatterns)urlpatterns = format_suffix_patterns(urlpatterns)urlpatterns = format_suffix_patterns(urlpatterns)0000000000000000urlpatterns = format_suffix_patterns(urlpatterns)urlpatterns = format_suffix_patterns(urlpatterns)urlpatterns = format_suffix_patterns(urlpatterns)urlpatterns = format_suffix_patterns(urlpatterns)urlpatterns = format_suffix_patterns(urlpatterns)urlpatterns = format_suffix_patterns(urlpatterns)urlpatterns = format_suffix_patterns(urlpatterns)urlpatterns = format_suffix_patterns(urlpatterns)urlpatterns = format_suffix_patterns(urlpatterns)urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns = [
    path('Register/', views. UserCreate.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('register/student/',views.StudentRegisterView.as_view()),
    path('register/teacher/',views.StudentRegisterView.as_view()),
    path('rest-auth/', include('rest_auth.urls'))

]
    #path(r'auth/', include('rest_auth.urls')),


urlpatterns = format_suffix_patterns(urlpatterns)