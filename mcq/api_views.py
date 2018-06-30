from rest_framework import viewsets, status
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from .models import Question, Answer, Tournament, TournamentParticipation
from .serializers import QuestionSerializer, QASerializer, TournamentSerializer


def calculate_score(questions, answers):
    score = 0
    for i in range(len(questions)):
        q_id = int(questions[i])
        a_id = int(answers[i])
        q = Question.objects.get(id=q_id)
        correct_id = None
        for a in q.answer_set.all():
            if a.correct:
                correct_id = a.id
                break
        if a_id == correct_id:
            score += 1
    return score


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @list_route(methods=['POST', ], url_path='answer')
    def answer(self, request):
        serializer = QASerializer(data=request.data)
        if serializer.is_valid():
            questions = serializer.data['questions']
            answers = serializer.data['answers']
            score = calculate_score(questions, answers)
            if request.user.id is not None:
                learner = request.user.learner_set.all()[0]
                learner.points += score
                learner.save()
            return_questions = []
            for i in range(len(questions)):
                temp_dict = {}
                q_id = int(questions[i])
                a_id = int(answers[i])
                q = Question.objects.get(id=q_id)
                correct_id = None
                for a in q.answer_set.all():
                    if a.correct:
                        correct_id = a.id
                        break
                temp_dict['q_id'] = q_id
                temp_dict['your_a_id'] = a_id
                temp_dict['correct_a_id'] = correct_id
                return_questions.append(temp_dict)
            return Response({'score': score, 'questions': return_questions}, status=status.HTTP_200_OK)


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

    @detail_route(methods=['POST', ], url_path='answer')
    def answer(self, request, pk):
        serializer = QASerializer(data=request.data)
        if serializer.is_valid():
            questions = serializer.data['questions']
            answers = serializer.data['answers']
            score = calculate_score(questions, answers)
            if request.user.id is not None:
                learner = request.user.learner_set.all()[0]
                learner.points += score * 5
                learner.save()
                t = Tournament.objects.get(id=pk)
                TournamentParticipation.objects.create(learner=learner, tournament=t, score=score)
            # return_questions = []
            # for i in range(len(questions)):
            #     temp_dict = {}
            #     q_id = int(questions[i])
            #     a_id = int(answers[i])
            #     q = Question.objects.get(id=q_id)
            #     correct_id = None
            #     for a in q.answer_set.all():
            #         if a.correct:
            #             correct_id = a.id
            #             break
            #     temp_dict['q_id'] = q_id
            #     temp_dict['your_a_id'] = a_id
            #     temp_dict['correct_a_id'] = correct_id
            #     return_questions.append(temp_dict)
            return Response(status=status.HTTP_200_OK)
