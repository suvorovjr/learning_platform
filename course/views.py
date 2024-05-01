from rest_framework import viewsets
from course.models import Course
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from lesson.permissions import IsAuthorOrModerator, IsAuthor, IsModerator
from course.serializers import CourseSerializer
from course.paginators import CoursePaginator
from subscription.models import Subscription
from course.tasks import notification_of_changes


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all().order_by('id')
    pagination_class = CoursePaginator

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action == 'list':
            permission_classes = [IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [IsAuthorOrModerator]
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsAuthor]
        elif self.action == 'destroy':
            permission_classes = [IsAuthor]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        subscribers = Subscription.objects.filter(course=instance.pk)
        subscribers_email = [subscriber.user.email for subscriber in subscribers]
        notification_of_changes.delay(instance.title, subscribers_email)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
