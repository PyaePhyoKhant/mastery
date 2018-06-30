from django.db import models


class Question(models.Model):
    question_text = models.TextField()
    correct_answer = models.ForeignKey('Answer', related_name='correct', blank=True, null=True)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text
