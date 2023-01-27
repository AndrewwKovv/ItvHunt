from rest_framework import viewsets
from .models import Vacancy, LowResultsSetPagination
from .serializers import VacancySerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
import django_filters.rest_framework




class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all().order_by('-id')
    serializer_class = VacancySerializer
    pagination_class = LowResultsSetPagination
    # permission_classes=[IsAuthenticatedOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


# /vacancy/{title_vacancy} - в основном урле
# /vacan/{title_vacancy}
# УРл можно дать имя name=vacancy  и ссылаться на  название
# и используем в редиректе reverse("vacancy", args = {title_vacancy}) она конструктор
#
#
#