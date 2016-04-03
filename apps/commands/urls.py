from rest_framework.routers import DefaultRouter

from .views import CommandViewSet, UserViewSet

router = DefaultRouter()
router.register('commands', CommandViewSet, base_name='commands')
router.register('users', UserViewSet)
