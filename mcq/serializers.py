from .models import Question, Answer
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
