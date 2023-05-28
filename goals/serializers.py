from .models import ActionPlan, Diary, Goal
from rest_framework import serializers

class GoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goal
        fields = '__all__'

class DiarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Diary
        fields = '__all__'
class ActionPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActionPlan
        fields = '__all__'