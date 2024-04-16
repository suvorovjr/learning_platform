from rest_framework import serializers
from lesson.serializers import LessonSerializer
from course.models import Course
from subscription.models import Subscription


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    @staticmethod
    def get_lesson_count(instance):
        if instance.lesson:
            return len(instance.lesson.all())

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        return user and Subscription.objects.filter(user=user, course=obj).exists()
