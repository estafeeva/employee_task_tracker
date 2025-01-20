from django.db import models


class Task(models.Model):
    """
    - Наименование
    - Ссылка на родительскую задачу (если есть зависимость)
    - Исполнитель
    - Срок
    - Статус
    - Дополнительные поля (по необходимости)

    я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]
    Привычка:
    Пользователь
    Место
    Время
    Действие
    Признак приятной привычки
    Связанная привычка
    Периодичность (по умолчанию ежедневная)
    Вознаграждение
    Время на выполнение
    Признак публичности
    """

    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.CASCADE
    )
    place = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        verbose_name="Место"
    )
    time = models.TimeField(null=True, blank=True, verbose_name="Время")
    action = models.CharField(
        max_length=150,
        verbose_name="Действие, которое представляет собой привычка"
    )
    is_pleasant_habit = models.BooleanField(
        default=False, verbose_name="Признак приятной привычки"
    )
    linked_habit = models.ForeignKey(
        "habits.Habit",
        null=True,
        blank=True,
        verbose_name="Связанная привычка",
        on_delete=models.SET_NULL,
    )
    period = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Периодичность"
    )  # количество дней, по умолчанию ежедневная
    reward = models.CharField(
        null=True, blank=True, max_length=150, verbose_name="Вознаграждение"
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name="Признак публичности"
    )
    duration = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Время выполнения"
    )  # Время выполнения должно быть не больше 120 секунд.
    last_date_of_execution = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата последнего выполнения"
    )

    def __str__(self):
        return f"Habit {self.action}"

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
