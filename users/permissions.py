from rest_framework.permissions import BasePermission


class IsModerStaff(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Moderator').exists():
            return True
        return False


class IsOwnerStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
