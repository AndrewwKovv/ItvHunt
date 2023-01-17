from rest_framework import viewsets
from .models import Company, LowResultsSetPagination
from .serializers import CompanySerializer
from rest_framework import filters





class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = LowResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']




