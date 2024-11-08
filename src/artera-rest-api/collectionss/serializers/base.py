from rest_framework.serializers import ModelSerializer
from collectionss.models import Collections

class CollectionsSerializer(ModelSerializer):
    class Meta:
        model = Collections 
        fields = '__all__'