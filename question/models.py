from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager
from commen_models import TimeBasedModel


# Create your models here.
class Field(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Question(TimeBasedModel, models.Model):
    class StatusChoices(models.TextChoices):
        OPEN = 'open', 'Open'
        PENDING = 'pending', 'Pending Answer'
        FINISHED = 'finished', 'Finished'
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='questions_author')
    image = models.ImageField()
    deadline = models.DateTimeField()
    tags = TaggableManager()
    fields = models.ManyToManyField(Field, related_name='questions_fields')
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.OPEN)

    def __str__(self):
        return self.title
