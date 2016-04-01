from rest_framework.viewsets import ModelViewSet

from .serializers import CommandSerializer
from .models import Command


class CommandViewSet(ModelViewSet):
    serializer_class = CommandSerializer

    def get_queryset(self):
        return Command.objects.filter(user=self.request.user)
