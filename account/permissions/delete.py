from rest_framework.permissions import BasePermission


class CanDelete(BasePermission):

    def has_permission(self, request, view, ):
        return request.user.account.branch.id == request.data.get("branch_id", None)
