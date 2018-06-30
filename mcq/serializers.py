from .models import Question, Answer, Tournament
from rest_framework import serializers


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answer_set = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        depth = 1
        fields = ('id', 'question_text', 'answer_set')

class TournamentSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Tournament
        fields = '__all__'
