from rest_framework import serializers
from .models import Artist, Albom, Songs, Country




class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"
        ref_name = "ArtistDetail"


class AlbomSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()

    class Meta:
        model = Albom
        fields = "__all__"
        ref_name = "AlbomDetail"


class SongsSerializer(serializers.ModelSerializer):
    albom = AlbomSerializer(read_only=True)

    class Meta:
        model = Songs
        fields = "__all__"
        ref_name = "SongsDetail"


class CountrySerializer(serializers.ModelSerializer):
    country = SongsSerializer(read_only=True)

    class Meta:
        model = Country
        fields = "__all__"

