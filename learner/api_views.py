from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response

from .serializers import LearnerSerializer
from .models import Learner


class LearnerViewSet(viewsets.ModelViewSet):
    queryset = Learner.objects.all().order_by('-points')
    serializer_class = LearnerSerializer

    @list_route(methods=['GET', ], url_path='score')
    def answer(self, request):
        pts = -1
        if request.user.id is not None:
            learner = request.user.learner_set.all()[0]
            pts = learner.points
        return Response({'points': pts}, status=status.HTTP_200_OK)
