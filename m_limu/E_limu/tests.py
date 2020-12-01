from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Quiz ,Question
from .serializers import QuizSerializer,QuestionSerializer


# initialize the APIClient app



class TestQuiz(APITestCase):
    def test_post_request_can_create_new_quiz(self):
        data = {
            "created": "2020-08-01T01:59:23.998Z", "updated": "2020-08-01T01:59:23.999Z", 
            "level": "2", "title": "Samsung Android", "slug": "samsung-android",
             "single_attempt": True, "pass_mark": 0, "success_text": "",
             "fail_text": "", "draft": False, "duration": "00:40:00",
            
        }

        response = self.client.post(reverse('E_learning_API.E_limu:quiz-list'), data=data)
        self.assertEqual(Quiz.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def get_all_quizes(self):
        response = self.client.get(reverse('E_learning_API.E_limu:quiz-list')),
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))



class TestQuestion(APITestCase):
    def test_post_can_create_new_question(self):
        data = {
            "quiz": 1,
        "question_text":" \\\\\\\\\\\n django",
        "hint": "",
        "choices": [
            {
                "choice": "d",
                "position": "a",
                "is_correct": False
            },
            {
                "choice": "hel",
                "position": "b",
                "is_correct":False
            },
            {
                "choice": "tu",
                "position": "c",
                "is_correct": False
            }
        ]  
        }

        response = self.client.post(reverse('E_learning_API.E_limu:questionlist'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), 1)



        