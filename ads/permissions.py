from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsOwner(BasePermission):
    message = 'Чужая собственность! Доступ закрыт!'

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'owner'):
            owner = obj.owner
        elif hasattr(obj, 'author'):
            owner = obj.author
        return owner == request.user


class IsStaff(BasePermission):
    message = 'Вы не админ/модератор'

    def has_permission(self, request, view):
        return request.user.role in [UserRoles.ADMIN, UserRoles.MODERATOR]
