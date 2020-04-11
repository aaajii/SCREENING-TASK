from agile.models import Category, Content
from rest_framework import serializers


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['category','order', 'item', 'details']
        extra_kwargs = {
            'category': {'write_only': True},
        }


class CategorySerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['name', 'content']
        
    
