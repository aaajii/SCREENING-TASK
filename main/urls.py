from django.urls import include, path, reverse_lazy
from django.contrib import admin
from django.views.generic import RedirectView

from rest_framework import routers
from agile import views

router = routers.DefaultRouter()
router.register('category', views.CategoryViewSet, basename='category')
router.register('content', views.ContentViewSet, basename='content')

urlpatterns = [
    path('',RedirectView.as_view(pattern_name='api-root')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls, name='admin'),

]
