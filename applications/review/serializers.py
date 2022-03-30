from rest_framework import serializers

from applications.review.models import Rating


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user_id'] = request.user.id
        review = Rating.objects.create(**validated_data)
        return review

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = f'{instance.user}'
        return rep



