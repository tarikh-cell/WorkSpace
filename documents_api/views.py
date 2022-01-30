from rest_framework import generics, permissions
from documents.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import DjangoModelPermissions, BasePermission
from rest_framework.views import APIView

class PostUserWritePermission(BasePermission):
    message = 'Permission Denied'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


# add postuserritepermission
class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CreatePost(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EditPost(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


    
