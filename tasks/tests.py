import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from tasks.models import Task

from django.urls import reverse


class TaskTestCase(APITestCase):
    # Задаем данные для тестов
    def setUp(self):
        self.task = Task.objects.create(
            name="Test1",
            deadline=(
                    datetime.datetime.now().astimezone() +
                    datetime.timedelta(days=2))
        )

    def test_task_retrieve(self):
        url = reverse("tasks:task-detail", args=(self.task.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.task.name)

    def test_task_create(self):
        url = reverse("tasks:task-list")
        data = {
            "name": "test",
        }
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.all().count(), 2)

    def test_task_update(self):
        url = reverse("tasks:task-detail", args=(self.task.pk,))
        data = {"name": "test2"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "test2")

    def test_task_delete(self):
        url = reverse("tasks:task-detail", args=(self.task.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.all().count(), 0)

    def test_task_list(self):
        url = reverse("tasks:task-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
