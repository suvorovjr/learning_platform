from rest_framework.permissions import BasePermission
from course.services import check_paid


class IsPaidCourse(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            user_id = request.user.id
            course_id = view.get_object().id
            return check_paid(user_id=user_id, course_id=course_id)
