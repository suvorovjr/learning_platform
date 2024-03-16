from rest_framework import serializers
from lesson.serializers import LessonSerializer
from course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    @staticmethod
    def get_lesson_count(instance):
        if instance.lesson:
            return len(instance.lesson.all())
