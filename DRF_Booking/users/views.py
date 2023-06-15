from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView

# from .models import Post
# from .serializers import PostSerializer
#
# from .models import Author, Book
# from .serializers import AuthorSerializer, BookSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'message': 'Username already exists'},
                            status=status.HTTP_409_CONFLICT)

        user = User.objects.create_user(username=username, password=password)
        token, _ = Token.objects.get_or_create(user=user)

        user.save()
        token.save()

        return Response({'token': token.key},
                        status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not User.objects.filter(username=username).exists():
            return Response({'message': 'Username does not exists'},
                            status=status.HTTP_404_NOT_FOUND)

        user = User.objects.get(username=username)

        if not user.check_password(password):
            return Response({'message': 'Incorrect password'},
                            status=status.HTTP_401_UNAUTHORIZED)

        token = Token.objects.get(user=user)

        return Response({'token': token.key},
                        status=status.HTTP_200_OK)