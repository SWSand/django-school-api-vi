from django.shortcuts import render
# from .models import Student
from .serializers import SubjectSerializer, Subject
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class All_subjects(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        ser_subs = SubjectSerializer(subjects)
        return Response(ser_subs.data)