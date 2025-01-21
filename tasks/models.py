from django.db import models


class Task(models.Model):
    """
    - Наименование
    - Ссылка на родительскую задачу (если есть зависимость)
    - Исполнитель
    - Срок (time)
    - Статус
    - Дополнительные поля (по необходимости)
    """

    name = models.CharField(
        null=True,
        blank=True,
        max_length=100,
        verbose_name="Наименование задачи"
    )
    parent_task_link = models.ForeignKey(
        "tasks.Task",
        null=True,
        blank=True,
        verbose_name="Связанная родительская задача",
        on_delete=models.SET_NULL,
    )
    responsible = models.ForeignKey(
        "tasks.Employee",
        null=True,
        blank=True,
        verbose_name="Исполнитель",
        on_delete=models.SET_NULL,
    )
    deadline = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Срок выполнения задачи"
    )

    CREATED = "Создана"
    STARTED = "Запущена"
    COMPLETED = "Завершена"

    STATUS_CHOICES = [
        (COMPLETED, "Завершена"),
        (CREATED, "Создана"),
        (STARTED, "Запущена"),
    ]

    status = models.CharField(
        max_length=150,
        choices=STATUS_CHOICES,
        default=CREATED,
        verbose_name="Статус"
    )

    def __str__(self):
        return f"Task {self.name}"

    class Meta:
        verbose_name = "задача"
        verbose_name_plural = "задачи"


class Employee(models.Model):
    """
    - ФИО
    - Должность
    - Дополнительные поля (по необходимости)
    """

    name = models.CharField(
        null=True,
        blank=True,
        max_length=150,
        verbose_name="ФИО"
    )

    position = models.CharField(
        null=True,
        blank=True,
        max_length=150,
        verbose_name="Должность"
    )

    def __str__(self):
        return f"Employee {self.name}"

    class Meta:
        verbose_name = "работник"
        verbose_name_plural = "работники"
