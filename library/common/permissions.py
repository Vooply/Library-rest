from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    For example user with role 1.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.role)


class IsOwnerOrAdmin(BasePermission):
    """
    Allows access only to admin or owner user
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj == request.user or request.user.role
