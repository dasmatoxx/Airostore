from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from applications.review.models import Rating
from applications.review.serializers import RatingSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated, ]
