from django.db import models


class Question(models.Model):
    question_text = models.TextField()
    correct_answer = models.ForeignKey('Answer', related_name='correct')

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text
