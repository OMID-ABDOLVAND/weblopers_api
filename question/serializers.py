from rest_framework import serializers
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)

from question.models import Question


class QuestionSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    author = serializers.SerializerMethodField()
    questions_fields = serializers.SerializerMethodField()

    def get_questions_fields(self, obj):
        return [field.name for field in obj.questions_fields.all()]

    def get_author(self, obj):
        return obj.author.username

    class Meta:
        model = Question
        fields = '__all__'
