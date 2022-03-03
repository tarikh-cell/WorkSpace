from rest_framework import generics, permissions
from productivity.models import Productivity
from .serializers import ProductivitySerializer
from rest_framework.permissions import DjangoModelPermissions, BasePermission
from rest_framework.views import APIView

class ProductivityList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Productivity.objects.all()
    serializer_class = ProductivitySerializer

    def get_queryset(self):
        user = self.request.user
        return Productivity.objects.filter(author=user)

class CreateProductivity(generics.CreateAPIView):
    print("here")
    permission_classes = [permissions.IsAuthenticated]
    queryset = Productivity.objects.all()
    serializer_class = ProductivitySerializer