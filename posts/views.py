from rest_framework import generics, permissions

from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializers
from .models import Post
# Create your views here.


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class Postdetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers
