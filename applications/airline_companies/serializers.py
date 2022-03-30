from cities_light.models import City
from rest_framework import serializers

from .models import Point, Plane, AviaCompany, Flight, AviaCompanyImage


class AviaCompanyImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = AviaCompanyImage
        fields = ('image', )

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = self._get_image_url(instance)
        return rep


class AviaCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = AviaCompany
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        total_rating = [i.rating for i in instance.review.all()]
        if len(total_rating) != 0:
            rep['total_rating'] = round(sum(total_rating) / len(total_rating), 1)

        else:
            rep['total_rating'] = ''

        rep['images'] = AviaCompanyImageSerializer(AviaCompanyImage.objects.filter(avia_company=instance.id), many=True,
                                               context=self.context).data
        return rep


class PointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Point
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['place_of_departure'] = instance.place_of_departure.title
        return rep


class PlaneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plane
        fields = '__all__'



class FlightSerializer(serializers.ModelSerializer):


    class Meta:
        model = Flight
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['avia_company'] = instance.avia_company.title
        rep['plane'] = instance.plane.title

        return rep


