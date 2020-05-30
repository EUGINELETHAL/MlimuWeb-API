from rest_framework import serializers
from .models import Subject, Course
from authentication.serializers import UserSerializer

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ('id', 'subject', 'title', 'slug', 'overview', 'created')


class SubjectSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = Subject
        fields = ('id', 'title', 'slug','courses')





 