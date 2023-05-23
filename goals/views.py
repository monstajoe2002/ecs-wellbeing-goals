from rest_framework import viewsets
# Create your views here.
from .models import Goal
from .serializers import GoalSerializer


class GoalViewSet(viewsets.ModelViewSet):

    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
