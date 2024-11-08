from rest_framework.serializers import ModelSerializer
from artworks.models import Artworks,ArtworkAdmin
from users.serializers import ProfileSerializer
from users.models import Profiles
from rest_framework import serializers

class ArtworksSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = Artworks 
        fields = '__all__'

class RegisterArtworkSerializer(ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=Profiles.objects.all(), required=False)

    class Meta:
        model = Artworks
        fields = [
            'artwork_type',
            'artwork_privacy',
            'artwork_name',
            'artwork_date',
            'artwork_images',
            'artwork_location',
            'artwork_description',
            'profile'
        ]

class ArtworkAdminSerializer(serializers.ModelSerializer):
    admin_user_profile_pic = serializers.SerializerMethodField()

    class Meta:
        model = ArtworkAdmin
        fields = ['admin_user_profile_pic']

    def get_admin_user_profile_pic(self, obj):
        return obj.admin_user.profile_picture_url  