from rest_framework import serializers
from frontend.models import NavMenu, DropdownMenu, AppData

class DropdownMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropdownMenu
        fields = ('id','name','icon','link')

class NavMenuSerializer(serializers.ModelSerializer):
    title = DropdownMenuSerializer(many=True)

    class Meta:
        model = NavMenu
        fields = ('id', 'name', 'icon', 'link', 'title')


class AppDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppData
        fields = ('app_name',)
