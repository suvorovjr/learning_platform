from rest_framework import viewsets
from course.models import Course
from rest_framework.permissions import IsAuthenticated
from lesson.permissions import IsAuthorOrModerator, IsAuthor
from course.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsAuthorOrModerator]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated, IsAuthorOrModerator]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsAuthor]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
