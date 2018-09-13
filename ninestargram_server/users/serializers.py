from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from . import models
from ninestargram_server.images import serializers as images_serializers


class UserProfileSerializer(serializers.ModelSerializer):
    images = images_serializers.CountImageSerializer(many=True, read_only=True)
    post_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    class Meta:
        model = models.User
        fields = (
            "username",
            "name",
            "bio",
            "website",
            "post_count",
            "followers_count",
            "following_count",
            "images",
            "profile_image",
        )


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ("id", "profile_image", "username", "name")
