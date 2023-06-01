from django.shortcuts import render
from products .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from products .models import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class DemoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
      print(request.user)
      return Response({"sucess" : "Hurray You are authenticated"})

class ProductView(APIView):
    def get(self, request):
      queryset = Product.objects.all()
      serialzer = ProductSerializer(queryset , many = True)
      return Response(serialzer.data)

