from rest_framework.routers import SimpleRouter

from tasks.apps import TasksConfig
from tasks.views import TaskViewSet, EmployeeViewSet

app_name = TasksConfig.name

router = SimpleRouter()
router.register(r"tasks", TaskViewSet, basename="task")
router.register(r"employees", EmployeeViewSet, basename="employee")

urlpatterns = [
    # path('', include(router.urls)),
]
urlpatterns += router.urls
