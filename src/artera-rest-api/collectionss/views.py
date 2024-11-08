from rest_framework.viewsets import ModelViewSet
from .serializers import CollectionsSerializer
from .models import Collections

# Create your views here.
class CollectionViewSet(ModelViewSet):
    """ 
    The API framework for creating the artwork.
    """
    queryset = Collections.objects.all()
    serializer_class = CollectionsSerializer
