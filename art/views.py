from rest_framework import viewsets
from .models import Artwork
from .serializers import ArtworkSerializer


class ArtworkViewset(viewsets.ModelViewSet):
  queryset = Artwork.objects.all()
  serializer_class = ArtworkSerializer
