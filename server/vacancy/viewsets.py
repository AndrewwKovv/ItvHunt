from rest_framework import viewsets
from .models import Vacancy, LowResultsSetPagination
from .serializers import VacancySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
import django_filters.rest_framework




class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    pagination_class = LowResultsSetPagination
    permission_classes=[IsAuthenticatedOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
