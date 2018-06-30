from django.contrib import admin
from .models import Question, Answer, Tournament, TournamentParticipation


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Tournament)
admin.site.register(TournamentParticipation)
