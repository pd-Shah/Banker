from rest_framework.routers import DefaultRouter

from .apis import (
    ViewSetUser,
)

router = DefaultRouter()
router.register(r'search', ViewSetUser, basename='search')

urlpatterns = router.urls
