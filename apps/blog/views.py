from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Post
from .serializers import PostListSerializer

# Create your views here.
class PostListView(ListAPIView):
  queryset = Post.postobjects.all()
  serializer_class = PostListSerializer

class PostDetailView(RetrieveAPIView):
  queryset = Post.postobjects.all()
  serializer_class = PostListSerializer
  lookup_field='slug'
