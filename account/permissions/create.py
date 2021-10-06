from rest_framework.permissions import BasePermission

from Banker.settings.permissions import ACCOUNT_CAN_CREATE_ALLOWED


class CanCreate(BasePermission):

    def has_permission(self, request, view):
        group_set = {g.name for g in request.user.groups.all()}
        if len(group_set.intersection(ACCOUNT_CAN_CREATE_ALLOWED)):
            return True
        return False
