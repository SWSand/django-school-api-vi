from django.shortcuts import render
# from .models import Student
from .serializers import StudentSerializer, Student
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class All_students(APIView):
    def get(self, request):
        students = Student.objects.all()
        ser_studs = StudentSerializer(students)
        return Response(ser_studs.data)