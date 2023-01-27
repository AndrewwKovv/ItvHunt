from rest_framework import serializers
from .models import Vacancy
# from candidate.models import Candidate

# class CandidateSerializerForVacancy(serializers.ModelSerializer):
#     class Meta:
#         model = Candidate
#         fields = ['email_candidate',]

class VacancySerializer(serializers.ModelSerializer):
    # candidate_email = CandidateSerializerForVacancy(source='candidate', many=True)
    class Meta:
        model = Vacancy
        fields = ['id', 'created_at', 'title', 'link_vacancy', 'candidate']
        # exclude = ['candidate']