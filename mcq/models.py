from django.db import models
from learner.models import Learner


class Question(models.Model):
    question_text = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    answer_text = models.CharField(max_length=100)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text


class Tournament(models.Model):
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField(auto_now_add=True)
    # unit is minute
    duration = models.IntegerField()
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return "{}: {} minute".format(self.title, self.duration)


class TournamentParticipation(models.Model):
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return "{} is in {} with {} points.".format(self.learner, self.tournament, self.score)

    class Meta:
        unique_together = ('learner', 'tournament')
