from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from .models import Post
from .serializer import PostSerializer


class PostViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer