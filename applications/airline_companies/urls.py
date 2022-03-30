from django.urls import path

from .views import PointView, PlaneView, FlightView, AviaCompanyView, AviaCompanyDetailView, FavoriteView

urlpatterns = [
    path('point/', PointView.as_view()),
    path('list-plane/', PlaneView.as_view()),
    path('list-avia-company/', AviaCompanyView.as_view()),
    path('list-avia-company/<int:pk>/', AviaCompanyDetailView.as_view()),
    path('company/<int:pk>/favorite/', FavoriteView.as_view()),
    path('list-flight/', FlightView.as_view()),
]
