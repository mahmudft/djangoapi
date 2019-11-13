from rest_framework import serializers
from store.models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'genre', 'artist', 'album', 'image', 'year']
