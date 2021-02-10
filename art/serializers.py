from rest_framework import serializers
from .models import Artwork


class ArtworkSerializer(serializers.HyperlinkedModelSerializer):
  url = serializers.HyperlinkedIdentityField(
      view_name='artwork-detail',
  )

  class Meta:
    model = Artwork
    fields = (
        'url',
        'id',
        'title',
        'year',
        'medium',
        'substrate',
        'size',
        'image')
