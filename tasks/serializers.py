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


class UrgentTaskSerializer(TaskSerializer):
    """
    2. Реализует поиск по сотрудникам, которые могут взять такие задачи
    (наименее загруженный сотрудник или
    сотрудник, выполняющий родительскую задачу,
    если ему назначено максимум на 2 задачи больше,
    чем у наименее загруженного сотрудника).
    """

    suitable_employee = serializers.SerializerMethodField()

    def get_suitable_employee(self, obj):

        """result = WorkloadEmployeesView.list(None)
        print(result)
        return True"""

        es = Employee.objects.all()
        min_workload_employee = None
        min_count = None
        for e in es:
            count = Task.objects.filter(responsible=e).count()
            if min_count is None or count < min_count:
                min_workload_employee = e
                min_count = count

        suitable_employee = min_workload_employee

        parent_task = obj.parent_task_link
        if parent_task:
            e2 = parent_task.responsible
            if e2:
                count_e2 = Task.objects.filter(responsible=e2).count()
                if count_e2 - min_count <= 2:
                    suitable_employee = e2

        return EmployeeSerializer(suitable_employee).data.get("name")

    class Meta:
        model = Task
        fields = ["name", "deadline", "suitable_employee"]


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class WorkloadSerializer(EmployeeSerializer):
    """
    Добавляет задачи сотрудников,
    и сортировку по количеству активных задач.

    """

    active_tasks = serializers.SerializerMethodField()
    active_tasks_count = serializers.SerializerMethodField()

    def get_active_tasks(self, obj):
        obj_tasks = Task.objects.filter(responsible=obj)
        return TaskSerializer(obj_tasks, many=True).data

    def get_active_tasks_count(self, obj):
        return Task.objects.filter(responsible=obj).count()
