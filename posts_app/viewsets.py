from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from . models import Post
from . serializers import PostSerializer

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]