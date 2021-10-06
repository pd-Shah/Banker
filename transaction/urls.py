from rest_framework.routers import DefaultRouter

from .apis import (
    ViewSetTransaction,
)

router = DefaultRouter()
router.register(r'transaction', ViewSetTransaction, basename='transaction')

urlpatterns = router.urls
