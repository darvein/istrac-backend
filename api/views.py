from rest_framework import generics
from .models import TPlace
from .serializers import TPlaceSerializer

class TPlaceListCreateView(generics.ListCreateAPIView):
    queryset = TPlace.objects.all()
    serializer_class = TPlaceSerializer

class TPlaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TPlace.objects.all()
    serializer_class = TPlaceSerializer
