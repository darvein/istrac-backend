from rest_framework import generics
from .models import TPlace, Photo, Video, Location, Category, Event, Like, Favorite, Comment
from .serializers import (TPlaceSerializer, PhotoSerializer, VideoSerializer, LocationSerializer, 
                          CategorySerializer, EventSerializer, LikeSerializer, FavoriteSerializer, CommentSerializer)

# TPlace Views
class TPlaceListCreateView(generics.ListCreateAPIView):
    queryset = TPlace.objects.all()
    serializer_class = TPlaceSerializer

    def get_serializer_context(self):
        return {'request': self.request}

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
