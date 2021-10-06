from django.urls import path
from rest_framework.routers import DefaultRouter

from .apis import (
    ViewSetCreateAccount,
    APIViewDeleteAccount,
)

router = DefaultRouter()
router.register(r'create', ViewSetCreateAccount, basename='account')

urlpatterns = router.urls

urlpatterns += [
    path(r'account/delete/', APIViewDeleteAccount.as_view(), name='delete-account'),
]
