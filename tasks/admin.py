from django.contrib import admin

from tasks.models import Task, Employee


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "parent_task_link",
        "responsible",
        "deadline",
        "status",
    )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "position")
