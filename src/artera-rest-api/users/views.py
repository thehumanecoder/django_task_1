from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_batteries.viewsets import GenericViewSet
from rest_batteries.mixins import RetrieveModelMixin, UpdateModelMixin
from django.contrib.auth.models import User
from django.db import transaction

from .models import Profiles
from .serializers import RegisterSerializer, ProfileSerializer

class AuthViewSet(viewsets.ViewSet):
    """
    A ViewSet for user registration and login, providing JWT tokens on successful actions.
    """
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], url_path='register')
    @transaction.atomic
    def register(self, request):
        """
        Register a new user and return JWT tokens.
        """
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        """
        Authenticate a user and provide JWT tokens.
        """
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email)
            if not user.check_password(password):
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class ProfileViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    """
    Allows users to retrieve and update their own profile only.
    """
    queryset = Profiles.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        """Override to ensure users only retrieve/update their own profile."""
        return Profiles.objects.get(user=self.request.user)