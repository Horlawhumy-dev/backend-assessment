from rest_framework import serializers
from .models import Task
import logging

logger = logging.getLogger('task_management')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        logger.debug(f"Creating task with data: {validated_data}")
        return super().create(validated_data)

    def update(self, instance, validated_data):
        logger.debug(f"Updating task id {instance.id} with data: {validated_data}")
        return super().update(instance, validated_data)
