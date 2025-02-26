from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import BlogSerializer
from .models import Blog

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

