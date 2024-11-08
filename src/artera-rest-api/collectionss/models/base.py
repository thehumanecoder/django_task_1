from django.db import models
from django.contrib.postgres.fields import ArrayField
from .types import CollectionTypeChoices, CollectionPrivacyChoices
import uuid

# Create your models here.

class Collections(models.Model):
    collection_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    collection_name = models.TextField(blank=False, null=False)
    collection_privacy = models.TextField(choices=CollectionPrivacyChoices.choices)
    collection_type = models.TextField(choices=CollectionTypeChoices.choices, default=CollectionTypeChoices.BY_USER)
    collection_banner = models.TextField(blank=True, null=True)
    collection_description = models.TextField(blank=True, null=True)
    collection_likes_counter = models.IntegerField(default=0)
    collection_artworks_counter = models.IntegerField(default=0)
    collection_admin_list = ArrayField(models.UUIDField(blank=True), blank=True, default=list)
    collection_images = models.JSONField(blank=True, null=True)