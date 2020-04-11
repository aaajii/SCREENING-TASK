from agile.models import Category, Content
from rest_framework import viewsets
from agile.serializers import CategorySerializer, ContentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
        API Viewset that displays the Category Model
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ContentViewSet(viewsets.ModelViewSet):
    """
        API Viewset that displays the Content Model
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
