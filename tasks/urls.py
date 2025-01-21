from django.urls import path

from rest_framework.routers import SimpleRouter

from tasks.apps import TasksConfig
from tasks.views import TaskViewSet, EmployeeViewSet, WorkloadEmployeesView, UrgentTasksView

app_name = TasksConfig.name

router = SimpleRouter()
router.register(r"tasks", TaskViewSet, basename="task")
router.register(r"employees", EmployeeViewSet, basename="employee")

urlpatterns = [
    # path('', include(router.urls)),
    path("workload/", WorkloadEmployeesView.as_view(), name="workload",),
    path("urgent_tasks/", UrgentTasksView.as_view(), name="urgent_tasks",),

]
urlpatterns += router.urls
