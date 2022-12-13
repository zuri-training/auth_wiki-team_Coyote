from rest_framework import generics, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from .serializers import *
# Create your views here.

class AuthLibraryView(viewsets.ModelViewSet):
    serializer_class = AuthLibrarySerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        # Return only the libraries created by the authenticated user
        return AuthLibrary.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        # Set the 'created_by' field to the authenticated user
        serializer.save(created_by=self.request.user)



class CommentAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        library_id = self.kwargs['library_id']
        return Comment.objects.filter(library_id=library_id)

    def perform_create(self, serializer):
        library_id = self.kwargs['library_id']
        library = AuthLibrary.objects.get(id=library_id)
        serializer.save(created_by=self.request.user, library=library)

