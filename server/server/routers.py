from rest_framework import routers
from task.viewsets import TaskViewSet
from authentication.viewsets import UserViewSet
from vacancy.viewsets import VacancyViewSet

router = routers.DefaultRouter()

router.register(r'task',  TaskViewSet)
router.register(r'authentication',  UserViewSet)
router.register(r'vacancy',  VacancyViewSet)


