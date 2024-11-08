from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status 

from .serializers import ArtworksSerializer,RegisterArtworkSerializer,ArtworkAdminSerializer
from .models import Artworks,ArtworkAdmin
from users.models import Profiles


class ArtworksViewSet(ModelViewSet):
    """ 
    The API framework for creating the artwork.
    """
    queryset = Artworks.objects.all()
    serializer_class = ArtworksSerializer


class CreateArtworkView(APIView):
    permission_class = [IsAuthenticated]

    def post(self,request):
        serializer = RegisterArtworkSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED )
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class AddArtworkAdminView(APIView):
    permission_class = [IsAuthenticated]

    def post(self,request,artwork_id):

        artwork = get_object_or_404(Artworks, pk= artwork_id)

        user_ids = request.data.get("user_ids",[])
        if not user_ids:
            return Response({"error":"No user IDs to update"}, status= status.HTTP_400_BAD_REQUEST)
        
        for user_id in user_ids:
            user = get_object_or_404(Profiles, pk= user_id)

            ArtworkAdmin.objects.get_or_create(
                artwork = artwork,
                admin_user = user,
                defaults= {'added_timestamp':timezone.now()}
            )

            artwork_serializer = ArtworkAdminSerializer(artwork)

            return Response(artwork_serializer.data, status = status.HTTP_200_OK)
