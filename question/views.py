from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet


# Create your views here.
from question.models import Question
from question.serializers import QuestionSerializer


class QuestionViewSet(mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

