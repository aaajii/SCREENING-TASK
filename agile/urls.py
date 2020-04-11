from django.urls import include, path
from rest_framework import routers
from agile import views

category_list = views.CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('', category_list, name="category"),

]
