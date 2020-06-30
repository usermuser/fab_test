from rest_framework import serializers

from .models import Poll, Question


class PollSerializer(serializers.Serializer):
    """
    For Create Poll operation
    """
    name = serializers.CharField(max_length=255)
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    description = serializers.CharField(max_length=255)
    questions = serializers.ListSerializer() # todo test this, here should be list of id's of questions

    def create(self, validated_data):
        return Poll.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class QuestionSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=300)
    poll_id = serializers.IntegerField()
    type = serializers.ChoiceField(choices=Question.CHOICES_TYPES)

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance
