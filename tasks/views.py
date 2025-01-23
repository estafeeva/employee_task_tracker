from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from tasks.models import Task, Employee
from tasks.serializers import (TaskSerializer,
                               EmployeeSerializer,
                               WorkloadSerializer,
                               UrgentTaskSerializer)


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class WorkloadEmployeesView(ListAPIView):
    """
    **Занятые сотрудники:**

    Запрашивает из БД список сотрудников и их задачи,
    отсортированный по количеству активных задач.

    """

    queryset = Employee.objects.all()
    serializer_class = WorkloadSerializer

    def list(self, request, *args, **kwargs):
        q = self.get_queryset()
        serializer = self.get_serializer(q, many=True)
        sorted_q = sorted(
            serializer.data,
            key=lambda x: x['active_tasks_count'],
            reverse=True
        )

        return Response(sorted_q)


class UrgentTasksView(ListAPIView):
    """
    **Важные задачи:**

    1. Запрашивает из БД задачи, которые не взяты в работу,
    но от которых зависят другие задачи, взятые в работу.

    2. Реализует поиск по сотрудникам, которые могут взять такие задачи
    (наименее загруженный сотрудник или
    сотрудник, выполняющий родительскую задачу,
    если ему назначено максимум на 2 задачи больше,
    чем у наименее загруженного сотрудника).

    3. Возвращает список объектов в формате:
    `{Важная задача, Срок, [ФИО сотрудника]}`.

    """

    #queryset = Task.objects.filter(
    #    status=Task.CREATED).exclude(parent_task_link=None)
    serializer_class = UrgentTaskSerializer

    """child_started = Task.objects.filter(
        status=Task.STARTED).exclude(parent_task_link=None)
    print(child_started)

    parent_pk_list_for_child_started = [item.parent_task_link.pk for item in child_started]
    print(parent_pk_list_for_child_started)

    # parent_not_started
    queryset = Task.objects.filter(
        status=Task.CREATED).filter(pk__in=parent_pk_list_for_child_started)
    print(queryset)"""

    def get_queryset(self):

        return Task.objects.filter(
            status=Task.CREATED).filter(
            pk__in=[
                item.parent_task_link.pk for item in
                Task.objects.filter(status=Task.STARTED
                                    ).exclude(parent_task_link=None)
            ]
        )
