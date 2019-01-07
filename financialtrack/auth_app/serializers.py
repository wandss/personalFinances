from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    """This serializer class is only used to proper raise exceptions.
    at a custom login view.
    """

    username = serializers.CharField()
    password = serializers.CharField()
