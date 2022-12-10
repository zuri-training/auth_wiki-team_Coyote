from .models import *
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.serializers import TokenObtainSerializer


# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response({
                "Message": "Your account has been successful created",
                "User": serializer.data}, status=status.HTTP_201_CREATED
            )

        return Response({"error": serializer._errors}, status=status.HTTP_400_BAD_REQUEST)
