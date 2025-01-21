from rest_framework.viewsets import ModelViewSet

from tasks.models import Task, Employee
from tasks.serializers import TaskSerializer, EmployeeSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
