from django.urls import path
from rest_framework.routers import DefaultRouter

from .apis import (
    APIViewTransaction,
    APIViewWithdraw,
    APIViewDeposit,
    ViewSetTransaction,
)

router = DefaultRouter()
router.register(r'search', ViewSetTransaction, basename='search')

urlpatterns = router.urls
urlpatterns += [
    path(r'transaction/', APIViewTransaction.as_view(), name='transaction'),
    path(r'withdraw/', APIViewWithdraw.as_view(), name='withdraw'),
    path(r'deposit/', APIViewDeposit.as_view(), name='deposit'),
]
