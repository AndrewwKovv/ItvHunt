from rest_framework import viewsets
from .models import Candidate, LowResultsSetPagination
from .serializers import CandidateSerializer



class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    pagination_class = LowResultsSetPagination


