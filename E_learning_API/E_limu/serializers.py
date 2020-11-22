from rest_framework import serializers
import itertools  
from .models import Choice, Question, Quiz, Course, Subject
from E_learning_API.authentication.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from E_learning_API.E_limu.serializers import *

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ('id', 'subject', 'title', 'slug', 'overview', 'created',)


class SubjectSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    
    class Meta:
        model = Subject
        fields = ('id', 'title', 'slug','courses')


# class ChoiceListSerializer(serializers.ListSerializer):
#     def create(self, validated_data):
#         books = [Book(**item) for item in validated_data]
#         return Book.objects.bulk_create(books)
#         class HighScoreSerializer(serializers.BaseSerializer):
    
# class HighScoreSerializer(serializers.BaseSerializer):
#     def to_internal_value(self, data):
#         choices = data.get('score')
#         player_name = data.get('player_name')

class ChoiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Choice
        fields = ('choice','is_correct')


    # def get_choice_types(self, obj):
    #         return Choice.choice_types(self)


    


    
        
    
       
        
        



class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    choice_types = serializers.SerializerMethodField()
    
    class Meta:
        model = Question
        fields = ('quiz', 'choice_types','question_text', 'hint', 'choices')
    
    def create(self, validated_data):
        # quiz = self.context['quiz']
        # print(quiz)
        choices_data = validated_data.pop('choices')
        NewQuestion = Question.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(question=NewQuestion, **choice_data)
        return NewQuestion

    def get_choice_types(self, obj):
           return obj.choice_types

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ('level', 'pk', 'title','slug', 'single_attempt','pass_mark','success_text','fail_text','draft','duration','questions')
    
    def create(self, validated_data):

        newQuiz = Quiz.objects.create(**validated_data)
        return newQuiz

 