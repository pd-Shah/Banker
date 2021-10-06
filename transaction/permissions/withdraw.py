from rest_framework.permissions import BasePermission


class CanWithdraw(BasePermission):

    def has_permission(self, request, view):
        return True
