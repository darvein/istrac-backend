from django.urls import path
from .views import TPlaceListCreateView, TPlaceDetailView, PhotoListCreateView

urlpatterns = [
    path('tplaces/', TPlaceListCreateView.as_view(), name='tplaces-list-create'),
    path('tplaces/<int:pk>/', TPlaceDetailView.as_view(), name='tplaces-detail'),
    path('photos/', PhotoListCreateView.as_view(), name='photos-list-create'),
]