from rest_framework import serializers
from lesson.serializers import LessonSerializers
from course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializers(source='lesson', many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, instance):
        if instance.lesson:
            return len(instance.lesson.all())
