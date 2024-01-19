from django.urls import path
from .views import TPlaceListCreateView, TPlaceDetailView, PhotoListCreateView, LocationListView, CategoryListView

urlpatterns = [
    path('tplaces/', TPlaceListCreateView.as_view(), name='tplaces-list-create'),
    path('tplaces/<int:pk>/', TPlaceDetailView.as_view(), name='tplaces-detail'),
    path('photos/', PhotoListCreateView.as_view(), name='photos-list-create'),
    path('locations/', LocationListView.as_view(), name='locations-list-create'),
    path('categories/', CategoryListView.as_view(), name='categories-list-create'),
]