from rest_framework import viewsets
from .serializers import LearnerSerializer
from .models import Learner


class LearnerViewSet(viewsets.ModelViewSet):
    queryset = Learner.objects.all().order_by('-points')
    serializer_class = LearnerSerializer
