from django.db import models
from taggit.managers import TaggableManager


# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=255)


class Question(models.Model):
    title = models.CharField(max_length=255, )
    description = models.TextField(max_length=1000, )
    image = models.ImageField()
    deadline = models.DateTimeField()
    tags = TaggableManager()
    fields = models.ManyToManyField(Field, related_name='questions_fields')

