from .models import Question, Answer, Tournament, TournamentParticipation
from rest_framework import serializers
from learner.serializers import LearnerSerializer


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


class QASerializer(serializers.Serializer):
    questions = serializers.ListField()
    answers = serializers.ListField()


class TournamentSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Tournament
        fields = '__all__'


class TournamentParticipationSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField('get_tournament_title')
    name = serializers.SerializerMethodField('get_learner_name')

    def get_tournament_title(self, obj):
        return obj.tournament.title

    def get_learner_name(self, obj):
        return obj.learner.name

    class Meta:
        model = TournamentParticipation
        depth = 1
        fields = ('id', 'score', 'name', 'title',)
