from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)  

urlpatterns = [
    path("api/", include(router.urls)),
]
