from rest_framework import serializers
from .models import Candidate
# from .models import User

# class UserSerializerForCandidate(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    # email_data = UserSerializerForCandidate(source='authentication', many=True)
    class Meta:
        model = Candidate
        fields = '__all__'
        # exclude = ['candidate_email']

       
