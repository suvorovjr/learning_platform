from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from users.models import User
from course.models import Course
from rest_framework import status
from subscription.models import Subscription
from django.urls import reverse


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='user@test.ru')
        self.user.set_password('testpassword')
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title='test_course',
            description='test_description',
            author=self.user
        )

    def test_create_subscription(self):
        """Тестирование создания подписки"""

        data = {
            'user': self.user.id,
            'course': self.course.id
        }

        response = self.client.post(
            '/subscription/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'message': 'Вы подписались на обновления курса'}
        )
