import datetime

from rest_framework import serializers


def validate_deadline(value):
    """Проверяет, что срок выполнения задачи не может быть в прошлом."""

    dt_now = datetime.datetime.now().astimezone()

    if value < dt_now:
        raise serializers.ValidationError(
            "Срок выполнения задачи не может быть в прошлом."
        )
