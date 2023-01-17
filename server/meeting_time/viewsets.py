from rest_framework import viewsets
from .models import MeetingTime
from .serializers import MeetingTimeSerializer
from rest_framework.permissions import IsAuthenticated


class MeetingTimeViewSet(viewsets.ModelViewSet):
    queryset = MeetingTime.objects.all()
    serializer_class = MeetingTimeSerializer
    permission_classes=[IsAuthenticated]