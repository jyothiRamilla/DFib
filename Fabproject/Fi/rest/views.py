from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import emp
from . serializers import empSerializer
from rest_framework import parsers, exceptions
from rest_framework.exceptions import ParseError



class empList(APIView):
    def get(self,request):
        emp1=emp.objects.all()
        serializer =empSerializer(emp1,many=True)
        return Response(serializer.data)