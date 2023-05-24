from rest_framework import viewsets
# Create your views here.
from .models import Diary, Goal
from .serializers import DiarySerializer, GoalSerializer


class GoalViewSet(viewsets.ModelViewSet):

    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class DiaryViewSet(viewsets.ModelViewSet):

    queryset = Diary.objects.all()
    serializer_class = DiarySerializer