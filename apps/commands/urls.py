from rest_framework.routers import DefaultRouter

from .views import CommandViewSet

router = DefaultRouter()
router.register('commands', CommandViewSet, base_name='commands')
