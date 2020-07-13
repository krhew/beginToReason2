"""
This module registers the models we created for the "core" application. After registering
the model, the data will be accessible through Django's admin functionality.
"""
from django.contrib import admin
from .models import Lesson, Reference, Reasoning, McChoice, Question, Code

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Reference)
admin.site.register(Reasoning)
admin.site.register(Question)
admin.site.register(McChoice)
admin.site.register(Code)