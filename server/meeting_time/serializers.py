from rest_framework import serializers
from .models import MeetingTime

class MeetingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingTime
        fields = ['id', 'free_time', 'close_time','candidates']