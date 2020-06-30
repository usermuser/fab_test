from rest_framework import serializers

from .models import Poll, Question


class PollSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Poll.objects.create(**validated_data)


class QuestionSerializer(serializers.Serializer):

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

