from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','password','email', 'last_login','first_name','bio','activity_role','company_title','is_active','is_staff','is_superuser',]