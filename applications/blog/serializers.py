from rest_framework import serializers

from .models import Question, Answer, Like


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'avia_company', 'title', 'question')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user.id
        question = Question.objects.create(**validated_data)
        return question

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['avia_company'] = instance.avia_company.title
        rep['author'] = instance.author.email
        rep['answer'] = AnswerSerializer(Answer.objects.filter(question=instance.id),
                                                                  many=True).data
        return rep


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'question', 'answer')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user.id
        answer = Answer.objects.create(**validated_data)
        return answer

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['like'] = instance.like.filter(like=True).count()
        return rep








