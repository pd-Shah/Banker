from rest_framework.routers import DefaultRouter

from .apis import (
    ViewSetUser,
)

router = DefaultRouter()

router.register(r'user', ViewSetUser, basename='user')

urlpatterns = router.urls
