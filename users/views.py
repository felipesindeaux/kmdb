from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404, render
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView, Response, status
from rest_framework.pagination import PageNumberPagination

from users.models import User
from users.permissions import UsersPermission
from users.serializers import LoginSerializer, RegisterSerializer


class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"]
        )

        if user:
            token = Token.objects.get_or_create(user=user)[0]

            return Response({"token": token.key})
        
        return Response(
            {"detail": "invalid email or password"}, status.HTTP_401_UNAUTHORIZED
        )

class UserView(APIView, PageNumberPagination):

    authentication_classes = [TokenAuthentication]
    permission_classes = [UsersPermission]

    def get(self, request):
        users = User.objects.all()

        result_page = self.paginate_queryset(users, request, view=self)

        serializer = RegisterSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

class UserViewById(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [UsersPermission]
    
    def get(self, request, id):
        user = get_object_or_404(User, pk=id)
        
        serializer = RegisterSerializer(user)

        return Response(serializer.data)
