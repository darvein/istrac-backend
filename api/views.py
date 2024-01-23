from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import TPlace, Photo, Video, Location, Category, Event, Like, Favorite, Comment
from .serializers import TPlaceSerializer, PhotoSerializer, VideoSerializer, LocationSerializer, CategorySerializer, EventSerializer, LikeSerializer, FavoriteSerializer, CommentSerializer

class TPlaceListCreateView(generics.ListCreateAPIView):
    serializer_class = TPlaceSerializer

    def get_queryset(self):
        queryset = TPlace.objects.all()
        location_name = self.request.query_params.get('location', None)

        # Check if location_name is provided and not 'default'
        if location_name and location_name.lower() != 'default':
            location = get_object_or_404(Location, slug__iexact=location_name)
            queryset = queryset.filter(location=location)

        # If location_name is 'default' or not provided, return all objects
        return queryset

class TPlaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TPlace.objects.all()
    serializer_class = TPlaceSerializer

# Photo Views
class PhotoListCreateView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

# Video Views
class VideoListCreateView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

# Location Views
class LocationListView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# Category Views
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Event Views
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# Like Views
class LikeListView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

# Favorite Views
class FavoriteListView(generics.ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

# Comment Views
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
