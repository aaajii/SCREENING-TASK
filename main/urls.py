from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from agile import views

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls), name='home'),
    path('admin/', admin.site.urls),

]
