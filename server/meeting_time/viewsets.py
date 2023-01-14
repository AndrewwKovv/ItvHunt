from rest_framework import viewsets
from .models import MeetingTime
from .serializers import MeetingTimeSerializer

class MeetingTimeViewSet(viewsets.ModelViewSet):
    queryset = MeetingTime.objects.all()
    serializer_class = MeetingTimeSerializer