from rest_framework import serializers

from tasks.models import Task, Employee
from tasks.validators import validate_deadline


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = "__all__"

    def validate(self, attrs):
        key = "deadline"

        if key in attrs:
            """если в словаре задано новое поле"""
            value = attrs.get(key)
            if value:
                validate_deadline(value)

        return attrs


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"
