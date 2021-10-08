from django.urls import path
from rest_framework.routers import DefaultRouter

from .apis import (
    APIViewCreateAccount,
    APIViewDeleteAccount,
)

router = DefaultRouter()
urlpatterns = router.urls
urlpatterns += [
    path(r'delete/', APIViewDeleteAccount.as_view(), name='delete-account'),
    path(r'create/', APIViewCreateAccount.as_view(), name='create-account'),
]
