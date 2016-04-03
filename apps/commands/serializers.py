from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Command

User = get_user_model()


class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email",
                  "pk", 'password', "username")
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        """
        Validate everything.
        """
        errors = {}
        # username is already checked by django
        # password is already checked by djago

        # Check email
        email = data.get("email", None)
        if email is None:
            errors['email'] = "Email cannot be empty"
            raise serializers.ValidationError(errors)

        return data
