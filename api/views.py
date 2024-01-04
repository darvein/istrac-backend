from rest_framework import generics
from .models import TPlace, Photo
from .serializers import TPlaceSerializer, PhotoSerializer

class TPlaceListCreateView(generics.ListCreateAPIView):
    queryset = TPlace.objects.all()
    serializer_class = TPlaceSerializer

    def get_serializer_context(self):
        return {'request': self.request}    

class TPlaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TPlace.objects.all()
    serializer_class = TPlaceSerializer

class PhotoListCreateView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
