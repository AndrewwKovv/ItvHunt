from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'created_at','update_at', 'title', 'desc', 'answer', 'language','completed']


    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()

        return instance

        
    def update(self, instance, validate_data):
        instance.title = validate_data.get('title', instance.title)
        instance.update_at = validate_data.get('update_at', instance.update_at)
        instance.desc = validate_data.get('desc', instance.desc)
        instance.answer = validate_data.get('answer', instance.answer)
        instance.language = validate_data.get('language', instance.language)
        instance.completed = validate_data.get('completed', instance.completed)
        instance.save()
        return  instance   