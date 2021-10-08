from rest_framework.permissions import BasePermission

from Banker.settings.permissions import TRANSACTION_CAN_SEARCH_ALLOWED


class CanSearch(BasePermission):

    def has_permission(self, request, view):
        group_set = {g.name for g in request.user.groups.all()}
        if len(group_set.intersection(TRANSACTION_CAN_SEARCH_ALLOWED)):
            return True
        return False
