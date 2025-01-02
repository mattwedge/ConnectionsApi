from rest_framework import serializers

from apps.authentication.models import User


class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)
