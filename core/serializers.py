from .models import List, Item
from rest_framework import serializers


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'url', 'List', 'name', 'done', 'created_at']


class ListSerializer(serializers.HyperlinkedModelSerializer):
    item_set = ItemSerializer(many=True)

    class Meta:
        model = List
        fields = ['id', 'url', 'user', 'name', 'item_set', 'created_at']
