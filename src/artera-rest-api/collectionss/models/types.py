from django.db import models

class CollectionPrivacyChoices(models.TextChoices):
    PUBLIC = 'public', 'Public'
    PRIVATE = 'private', 'Private'

class CollectionTypeChoices(models.TextChoices):
    BY_USER = 'by_user', 'By User'
    BY_ARTIST = 'by_artist', 'By Artist'
    BY_INSTITUTION = 'by_institution', 'By Institution'
    EXHIBITION = 'exhibition', 'Exhibition'
    DISCOVER = 'discover', 'Discover'
    YOUR_LIKED_ARTWORKS = 'your_liked_artworks', 'Your Liked Artworks'