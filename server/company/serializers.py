from rest_framework import serializers
from .models import Company
# from vacancy.models import Vacancy

# class VacancySerializerForCompany(serializers.ModelSerializer):
#     class Meta:
#         model = Vacancy
#         fields = ['title',]

class CompanySerializer(serializers.ModelSerializer):
    # title_vacancy = VacancySerializerForCompany(source='vacancy', many=True)
    class Meta:
        model = Company
        fields = '__all__'
        # exclude = ['vacancies']