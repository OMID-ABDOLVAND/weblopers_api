from rest_framework import serializers
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from taggit.models import Tag
from question.models import Question, Field
class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ('name',)

class QuestionSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    author = serializers.SerializerMethodField()
    # questions_fields = FieldieldSerializer()

    def get_author(self, obj):
        return obj.author.username

    class Meta:
        model = Question
        fields = '__all__'

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

