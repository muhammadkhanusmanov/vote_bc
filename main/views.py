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
