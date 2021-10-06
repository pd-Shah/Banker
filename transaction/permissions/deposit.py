from rest_framework.permissions import BasePermission


class CanDeposit(BasePermission):

    def has_permission(self, request, view):
        return True
