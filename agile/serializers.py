from agile.models import Category, Content
from rest_framework import serializers


class ContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Content
        fields = ['order', 'item', 'details']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    content = ContentSerializer(many=True)

    class Meta:
        model = Category
        fields = ['name', 'content']
