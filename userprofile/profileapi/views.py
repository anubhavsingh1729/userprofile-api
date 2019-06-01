from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated

from . import permission
from .models import userProfile,ProfileFeedItem
from . import serialize
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

class HelloViewset(viewsets.ViewSet):
    serializer_class = serialize.HelloSerializer
    def list(self,request):
        a_list = ['viewset item list','uses action (list, create, update, retrieve, partial update) ']
        return Response({"message":a_list})

    def create(self,request):
        serializer = serialize.HelloSerializer(data = request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({"message":message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk =None):
        return Response({'http_method':'Put'})

    def retrieve(self,request,pk =None):
        return Response({'http_method':'Get'})

    def partial_update(self,request,pk =None):
        return Response({'http_method':'Patch'})
        
    def destroy(self,request,pk = None):
        return Response({'http_method':'Delete'})
    
class userProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serialize.userProfileSerializer
    queryset = userProfile.objects.all()
    permission_classes = (permission.UpdateOwnProfile,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email')

class LoginViewSet(viewsets.ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self,request):
        return ObtainAuthToken().post(request)

class ProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serialize.ProfileFeedSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (permission.UpdateOwnFeed,IsAuthenticated)

    def perform_create(self,serializer):
        serializer.save(user_profile=self.request.user)