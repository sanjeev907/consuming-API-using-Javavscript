from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.

def home(request):
 return render(request,'form.html')
 
class PatientView(generics.GenericAPIView):
 def get(self,request):
  pat= Patient.objects.all()
  serializers = PatientSerializer(pat,many=True)
  return Response(serializers.data)


class PatientPostView(generics.GenericAPIView):
 def post(self,request):
  serializers = PatientSerializer(data=request.data)
  if serializers.is_valid():
   Patient.objects.create(name= serializers.data['name'],age=serializers.data['age'],test= serializers.data['test'],B2B_price=serializers.data['B2B_price'],status=serializers.data['status'],B2C_price=serializers.data['B2C_price'],B2C_Status=serializers.data['B2C_Status'])
   return Response(serializers.data)
  else:
   return Response(serializers.errors)