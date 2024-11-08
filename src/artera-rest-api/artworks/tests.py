from django.urls import reverse 
from rest_framework.test import APITestCases 
from rest_framework import status
from django.test import TestCase


from artworks.models import Artworks,ArtworkAdmin
from users.models import Profiles

import uuid
# Create your tests here.
class CreateArtworkViewTests(APITestCases):

    def setup(self):
        self.user = Profiles.objects.create(email="johndoe@gmail.com",password="password",profile_handle="johndoe")
        self.client.force_authenticate(user=self.user)
        self.create_artwork_url = reverse('create-artwork')

    def create_artwork_success(self):
        data = {
            "artwork_type":"painting",
            "artwork_privacy":"public",
            "artwork_name":"Monalisa",
            "artwork_date":"2024-11-08T11:32:00Z",
            "artwork_description":"Lorem epsum set emet,dollar",
            "artwork_location":"London,UK"
        }

        response = self.client.post(self.create_artwork_url,data,format="json")
        self.assertEqual(response.status_code , status.HTTP_201_CREATED)
        self.assertEqual(Artworks.objects.count(),1)
        self.assertEqual(response.data.get('artwork_name'), data.get('artwork_name'))

    def test_case_for_missing_fields(self):
        data = {
            "artwork_type":"painting",
            "artwork_name":""
        }

        response = self.client.post(self.create_artwork_url,data,format="json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)