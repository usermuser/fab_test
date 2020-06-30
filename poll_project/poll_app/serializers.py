from rest_framework import serializers


class PollSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class QuestionSerializer(serializers.Serializer):
    pass

