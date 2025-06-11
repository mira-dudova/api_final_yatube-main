from rest_framework import permissions

class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Разрешила доступ на чтение для всех, создание и изменение только для аутентифицированных
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Разрешила изменение только автору
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
