from rest_framework.permissions import BasePermission


class CanWithdraw(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if hasattr(user, "account"):
            if user.account.is_active:
                value = request.data.get("value", None)
                if value is not None:
                    if int(user.account.balance) > int(value):
                        return True
        return False
