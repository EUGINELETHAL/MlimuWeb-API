from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Subject, Course
from .serializers import SubjectSerializer, CourseSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics

class SubjectList(APIView):
    def get(self, request, format=None):
        all_subjects = Subject.objects.all()
        serializers = SubjectSerializer(all_subjects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = SubjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SubjectDetail(APIView):
        """
    Retrieve, update or delete a subject instance.
    """
        def get_object(self, pk):
            try:
                return Subject.objects.get(pk=pk)
            except Subject.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            subject = self.get_object(pk)
            serializer = SubjectSerializer(subject)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            subject = self.get_object(pk)
            serializer = SubjectSerializer(subject, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            def delete(self, request, pk, format=None):
                subject = self.get_object(pk)
                subject.delete()
                return Response(status=status.HTTP_204_NO_CONTENT) 


# class CourseList(APIView):
    
#     def get(self, request, format=None):
#         all_courses = Course.objects.filter(owner=self.request.user)
#         serializers = CourseSerializer(all_courses, many=True)
#         return Response(serializers.data)

#     def post(self, request, format=None):
#         serializers = CourseSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save(instructor=self.request.user)
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request, pk):
    """
    Retrieve, update or delete a single course.
    """
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseEnrollView(APIView):
    def post(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return Response({'enrolled': True})        