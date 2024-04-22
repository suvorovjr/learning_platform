from rest_framework.permissions import BasePermission


class IsAuthorOrModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='manager').exists():
            return True
        return request.user == view.get_object().author


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        return request.user == view.get_object().author


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='manager').exists():
            return True


class IsPaid(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='manager').exists():
            return True
        return request.user == view.get_object().author
