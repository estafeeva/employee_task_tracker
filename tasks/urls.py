from rest_framework.routers import SimpleRouter

from tasks.apps import TasksConfig

app_name = TasksConfig.name

"""router = SimpleRouter()
router.register(r"habits", HabitViewSet, basename="habit")
router.register(r"public", PublicViewSet, basename="public")"""

urlpatterns = [
    # path('', include(router.urls)),
]
#urlpatterns += router.urls
