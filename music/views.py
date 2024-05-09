import json
from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Artist, Albom, Songs
from .models import Artist, Albom, Songs, Country


from .serializers import ArtistSerializer,  SongsSerializer,AlbomSerializer, CountrySerializer

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = '__all__'

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = '__all__'


class LandingPageAPIView(APIView):
    def get(self, request):
        return Response(data={"message": "Hi Maqsud developers"})

    def post(self, request):
        return Response(data={"post api": "this is post apiii"})


class ArtistApiView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serialisers = ArtistSerializer(artists, many=True)
        return Response(data=serialisers.data)


class AlbomAPIViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer





class SongSetAPIView(ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    authentication_classes = (TokenAuthentication, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['^title']
    pagination_class = LimitOffsetPagination

    # pagination_class = LimitOffsetPagination



class CountrySetApiView(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['^title']
    pagination_class = LimitOffsetPagination
