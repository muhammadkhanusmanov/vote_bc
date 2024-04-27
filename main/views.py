from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.http import HttpRequest,JsonResponse,FileResponse
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication, BasicAuthentication

from .models import Polls

from .serialzer import PollSerializer 



class UserView(APIView):
    """Create a new user"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    def post(self, request):
        data = request.data
        username = data.get('username',None)
        password = data.get('password',None)
        first_name = data.get('first_name',None)
        try:
            user = User.objects.create(
                username=username,
                password=make_password(password),
                first_name=first_name
            )
            user.save()
            token,created = Token.objects.get_or_create(user=user)  
            return Response({'token':token.key},status=status.HTTP_201_CREATED)
        except:
            return Response({'status':'The username already exist'},status=status.HTTP_400_BAD_REQUEST)
    
    '''Delete a user'''
    def delete(self, username):
        data = self.request.data
        user_id = data['user_id']
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return Response({'status':'The user has been deleted'},status=status.HTTP_200_OK)
        except:
            return Response({'status':'The user was not found'},status=status.HTTP_400_BAD_REQUEST)

class UserLogin(models.Model):
    '''the function for authenticating a user'''
    authentication_classes = [BasicAuthentication]
    def post(self, request):
        user = request.user
        token = Token.objects.get_or_create(user=user)
        return Response({'status':True,'token':token.key},status=status.HTTP_200_OK)

class PollView(APIView):
    '''Create a new poll'''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    """Create a new poll"""
    def post(self, request):
        data = request.data
        try:
            poll = Polls.objects.create(
                poll_que=data.get('poll_que', None),
                que1=data.get('que1', None),
                que2=data.get('que2', None),
                que3=data.get('que3', None),
                que4=data.get('que4', None),
                que5=data.get('que5', None),
                que6=data.get('que6', None),
                que7=data.get('que7', None),
                time=data.get('time', None)
            )
            poll.save()
            return Response({'status':True},status=status.HTTP_201_CREATED)
        except:
            return Response({'status':False},status=status.HTTP_400_BAD_REQUEST)

    '''delete the poll'''
    def delete(self, request,id:str):
        try:
            poll = Polls.objects.get(id=id)
            poll.delete()
            return Response({'status':True},status=status.HTTP_200_OK)
        except:
            return Response({'status':False},status=status.HTTP_400_BAD_REQUEST)

