from .models import Goal
from rest_framework import serializers

class GoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goal
        fields = '__all__'