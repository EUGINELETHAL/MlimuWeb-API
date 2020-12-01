from rest_framework import serializers
from .models import Choice, Question, Quiz, Course, Subject
from E_learning_API.authentication.serializers import UserSerializer
from django.shortcuts import get_object_or_404


class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ('id', 'subject', 'title', 'slug', 'overview', 'created',)


class SubjectSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    
    class Meta:
        model = Subject
        fields = ('id', 'title', 'slug','courses')


class ChoiceSerializer(serializers.ModelSerializer):
    choice_type = serializers.SerializerMethodField()
    class Meta:
        model = Choice
        fields = ('choice','position','is_correct','choice_type',)

    def get_choice_type(self, obj):
        choice_letters = ['a', 'b', 'c','d']
        print(obj.question.id)
        question=Question.objects.get(id=obj.question.id)
        if question.id==11:
            for choice in question.choices.all():
                return choice.id
        else:
            return obj.question.id

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    class Meta:
        model = Question
        fields = ('id','quiz', 'question_text', 'hint', 'choices',)

    
        
    def create(self, validated_data):
        # quiz = self.context['quiz']
        # print(quiz)
        new_choices=[]
        choices_data = validated_data.pop('choices')
        print(len(choices_data))
        if len(choices_data)<4:
            raise serializers.ValidationError('You must enter 4 choices.')
        NewQuestion = Question.objects.create(**validated_data)
        for choice_data in choices_data:
            print(choice_data)
            Choice.objects.create(question=NewQuestion, **choice_data)
        return NewQuestion


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ('level', 'pk', 'title','slug', 'single_attempt','pass_mark','success_text','fail_text','draft','duration','questions')
    
    def create(self, validated_data):

        newQuiz = Quiz.objects.create(**validated_data)
        return newQuiz

 