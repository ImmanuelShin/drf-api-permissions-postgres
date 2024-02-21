from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner is None:
            return True

        return request.user.is_superuser or obj.owner.id == request.user.id