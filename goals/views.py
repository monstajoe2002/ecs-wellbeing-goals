from rest_framework import viewsets
# Create your views here.
from .models import ActionPlan, Diary, Goal
from .serializers import ActionPlanSerializer, DiarySerializer, GoalSerializer


class GoalViewSet(viewsets.ModelViewSet):

    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class DiaryViewSet(viewsets.ModelViewSet):

    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    
class ActionPlanViewSet(viewsets.ModelViewSet):

    queryset = ActionPlan.objects.all()
    serializer_class = ActionPlanSerializer