from rest_framework import routers
from task.viewsets import TaskViewSet
from authentication.viewsets import UserViewSet
from vacancy.viewsets import VacancyViewSet
from candidate.viewsets import CandidateViewSet
from company.viewsets import CompanyViewSet
from meeting_time.viewsets import MeetingTimeViewSet

router = routers.DefaultRouter()

router.register(r'task',  TaskViewSet)
router.register(r'auth',  UserViewSet)
router.register(r'vacancy',  VacancyViewSet)
router.register(r'candidate',  CandidateViewSet)
router.register(r'company',  CompanyViewSet)
router.register(r'meeting_time',  MeetingTimeViewSet)




