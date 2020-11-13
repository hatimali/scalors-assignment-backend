from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, TODOViewSet, ReminderViewSet

router = DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'todos', TODOViewSet)
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
