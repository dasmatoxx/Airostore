from rest_framework import generics, status, filters
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView

from .models import Point, Plane, AviaCompany, Flight
from .serializers import PointSerializer, PlaneSerializer, FlightSerializer, AviaCompanySerializer
from ..account.models import Profile


class FlightPriceFilter(rest_framework.FilterSet):
    min_price = rest_framework.NumberFilter(field_name='price',
                                            lookup_expr='gte')
    max_price = rest_framework.NumberFilter(field_name='price',
                                            lookup_expr='lte')

    class Meta:
        model = Flight
        fields = [
            'min_price',
            'max_price',
        ]


class AviaCompanyView(ListAPIView):
    queryset = AviaCompany.objects.all()
    serializer_class = AviaCompanySerializer


class PointView(ListAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class PlaneView(ListAPIView):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer


class FlightView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = FlightPriceFilter
    search_fields = ['plane', ]

    def get_serializer_context(self):
        return {'request': self.request}


class AviaCompanyDetailView(generics.RetrieveAPIView):
    queryset = AviaCompany.objects.all()
    serializer_class = AviaCompanySerializer


class FavoriteView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, pk):
        profile = Profile.objects.get(user=request.user.id)
        if profile.favorite.filter(id=pk).exists():
            profile.favorite.set(profile.favorite.exclude(id=pk))
            msg = 'AviaCompany was deleted from favorites!'
        else:
            profile.favorite.add(pk)
            profile.save()
            msg = 'AviaCompany added to favorite successfully!'
        return Response(msg, status=status.HTTP_200_OK)
