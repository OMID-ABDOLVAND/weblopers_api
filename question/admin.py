from django.contrib import admin

# Register your models here.
from question.models import Question, Field

admin.site.register(Question)
admin.site.register(Field)
