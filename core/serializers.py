from .models import List
from rest_framework import serializers


class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ['url', 'user', 'name']
