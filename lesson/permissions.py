from rest_framework.permissions import BasePermission


class IsAuthorOrModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator').exists():
            return True
        return request.user == view.get_object().author


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        return request.user == view.get_object().author
