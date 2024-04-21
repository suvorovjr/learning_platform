from rest_framework import generics
from lesson.models import Lesson
from lesson.serializers import LessonSerializer
from lesson.permissions import IsAuthorOrModerator, IsAuthor, IsModerator, IsPaid
from rest_framework.permissions import IsAuthenticated
from lesson.paginators import LessonPaginator
from rest_framework.exceptions import NotFound, PermissionDenied
from course.models import Course


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


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthor]
