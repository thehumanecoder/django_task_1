from django.urls import path 
from artworks.views import CreateArtworkView,AddArtworkAdminView

urlpatterns = [
    path('artworks/create/',CreateArtworkView.as_view(),name='create-art-work'),
    path('artworks/<uuid:artwork_id>/add_admin/',AddArtworkAdminView.as_view(),name='add-admin-to-artwork')
]