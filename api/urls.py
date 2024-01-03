from django.urls import path
from .views import TPlaceListCreateView, TPlaceDetailView

urlpatterns = [
    path('tplaces/', TPlaceListCreateView.as_view(), name='tplaces-list'),
    path('tplaces/<int:pk>/', TPlaceDetailView.as_view(), name='tplaces-detail')
]
