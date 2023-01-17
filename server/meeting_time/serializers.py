from rest_framework import serializers
from .models import MeetingTime
from candidate.models import Candidate

class CandidateSerializerForVacancy(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['email_candidate',]

class MeetingTimeSerializer(serializers.ModelSerializer):
    candidate_email = CandidateSerializerForVacancy(source='candidate', many=True)
    class Meta:
        model = MeetingTime
        # fields = ['id', 'free_time', 'close_time','candidates',]
        exclude = ['candidates']