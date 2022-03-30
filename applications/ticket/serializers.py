from rest_framework import serializers

from .models import TypeClass, TicketBook
from ..airline_companies.models import Flight
from ..airline_companies.serializers import FlightSerializer


class TypeClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeClass
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(many=False)
    type = TypeClassSerializer(many=False)
    user = serializers.CharField(required=False)

    class Meta:
        model = TicketBook
        fields = ('type', 'flight', 'user', 'last_name', 'first_name',
                  'middle_name', 'date_of_birth', 'passport_id',
                  'period_of_validity', 'issued_passport', 'seat', 'total_price', 'status')


class TicketBookSerializer(serializers.ModelSerializer):
    user = serializers.CharField(required=False)

    class Meta:
        model = TicketBook
        fields = ('type', 'flight', 'user', 'last_name', 'first_name',
                  'middle_name', 'date_of_birth', 'passport_id',
                  'period_of_validity', 'issued_passport', 'seat')