from .models import Learner
from rest_framework import serializers


class LearnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Learner
        fields = '__all__'
