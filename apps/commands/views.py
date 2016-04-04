from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token

from .serializers import CommandSerializer, UserSerializer
from .models import Command

User = get_user_model()


class CommandViewSet(ModelViewSet):
    serializer_class = CommandSerializer

    def get_queryset(self):
        return Command.objects.filter(user=self.request.user)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new user \o/
        """
        userSerializer = UserSerializer(data=request.data)
        if userSerializer.is_valid():
            user = User.objects.create_user(**userSerializer.validated_data)
            user.set_password(userSerializer.validated_data['password'])
            user.save()
            token = Token.objects.get_or_create(user=user)[0]
            return Response({"token": token.key}, status.HTTP_201_CREATED)
        return Response(userSerializer.errors, status.HTTP_400_BAD_REQUEST)
