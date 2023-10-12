from django.shortcuts import render
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

# Create your views here.
from question.models import Question
from question.serializers import QuestionSerializer


class QuestionFilter(django_filters.FilterSet):
    tags = django_filters.CharFilter(field_name='tags__name', lookup_expr='icontains')
    questions_fields = django_filters.CharFilter(field_name='questions_fields__name', lookup_expr='icontains')

    class Meta:
        model = Question
        fields = ['tags', 'questions_fields', 'status', 'title']


class CustomPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 50


class QuestionViewSet(mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['deadline', 'created_at']
    filterset_class = QuestionFilter
