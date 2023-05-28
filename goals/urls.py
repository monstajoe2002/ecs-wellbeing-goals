from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'goals', views.GoalViewSet)
router.register(r'diaries', views.DiaryViewSet)
router.register(r'action-plans', views.ActionPlanViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('goals-module/', include(router.urls)),

]
