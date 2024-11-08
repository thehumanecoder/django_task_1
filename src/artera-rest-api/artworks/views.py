from rest_framework.viewsets import ModelViewSet
from .serializers import ArtworksSerializer
from .models import Artworks

class ArtworksViewSet(ModelViewSet):
    """ 
    The API framework for creating the artwork.
    """
    queryset = Artworks.objects.all()
    serializer_class = ArtworksSerializer
