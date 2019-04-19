from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import userProfile 
from . import serialize
from rest_framework import status
# Create your views here.

class HelloApi(APIView):
    serializer_class = serialize.HelloSerializer

    def get(self,request,format=None):
        apilist = ["list_item1","list_item2","list_item3","list_item4"]
        return Response({'message':apilist})
    
    def post(self,request):
        serializer = serialize.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk = None):
        return Response({'message':'put'})

    def patch(self,request,pk = None):
        return Response({'message':'patch'})

    def delete(self,request,pk = None):
        return Response({'message':'delete'})