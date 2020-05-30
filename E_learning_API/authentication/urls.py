from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('Register/', views. UserCreate.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('register/student')
    path('rest-auth/', include('rest_auth.urls'))

]
    #path(r'auth/', include('rest_auth.urls')),


urlpatterns = format_suffix_patterns(urlpatterns)