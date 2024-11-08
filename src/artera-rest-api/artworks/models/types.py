from django.db import models

class ArtworkPrivacyChoices(models.TextChoices):
    PUBLIC = 'public', 'Public'
    PRIVATE = 'private', 'Private'

class ArtworkTypeChoices(models.TextChoices):
    IMAGE = 'image', 'By image'
    VIDEO = 'video', 'By video'
    MODEL = 'model', 'By model'
