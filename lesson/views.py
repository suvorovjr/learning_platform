from rest_framework import generics
from rest_framework.response import Response
from course.tasks import notification_of_changes
from lesson.models import Lesson
from lesson.serializers import LessonSerializer
from lesson.permissions import IsAuthorOrModerator, IsAuthor, IsModerator, IsPaid
from rest_framework.permissions import IsAuthenticated
from lesson.paginators import LessonPaginator
from rest_framework.exceptions import PermissionDenied
from course.models import Course
from subscription.models import Subscription


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        course_id = self.request.data.get('course')
        course = Course.objects.get(id=course_id)
        if course.author == self.request.user:
            new_lesson = serializer.save()
            new_lesson.author = self.request.user
            new_lesson.save()
        else:
            raise PermissionDenied({'message': 'Только автор курса может добавлять уроки.'})


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all().order_by('id')
    permission_classes = [IsAuthenticated]
    pagination_class = LessonPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthorOrModerator, IsPaid]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthorOrModerator]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        subscribers = Subscription.objects.filter(course=instance.course.pk)
        subscribers_email = [subscriber.user.email for subscriber in subscribers]
        notification_of_changes.delay(instance.title, subscribers_email)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthor]
