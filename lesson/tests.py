from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from users.models import User
from lesson.models import Lesson
from course.models import Course


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

        self.lesson = Lesson.objects.create(
            title='test_lesson_1',
            description='test_description_1',
            video_link='https://www.youtube.com/watch?v=6EdAg5FdsGw',
            course=self.course,
            author=self.user
        )

    def test_create_lesson(self):
        """Тест создания урока"""

        data = {
            'title': 'test_lesson',
            'description': 'test_description',
            'video_link': 'https://www.youtube.com/watch?v=6EdAg5FdsGw',
            'course': self.course.id,
            'author': self.user.id
        }
        response = self.client.post(
            reverse('lesson:create'),
            data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.json(),
            {'id': 2, 'title': 'test_lesson', 'imagine': None, 'description': 'test_description',
             'video_link': 'https://www.youtube.com/watch?v=6EdAg5FdsGw', 'course': self.course.id,
             'author': self.user.id}
        )

    def test_list_lesson(self):
        """Тест вывода списка уроков"""

        response = self.client.get(
            reverse('lesson:list')
        )

        body = {'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {'id': self.lesson.id,
                     'title': 'test_lesson_1',
                     'imagine': None,
                     'description': 'test_description_1',
                     'video_link': 'https://www.youtube.com/watch?v=6EdAg5FdsGw',
                     'course': self.course.id,
                     'author': self.user.id
                     }
                ]
                }

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            body
        )

    def test_view_lesson(self):
        """Тест отображения одного урока"""

        response = self.client.get(
            reverse('lesson:view', args=[str(self.lesson.id)])
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        body = {
            'id': self.lesson.id,
            'title': 'test_lesson_1',
            'imagine': None,
            'description': 'test_description_1',
            'video_link': 'https://www.youtube.com/watch?v=6EdAg5FdsGw',
            'course': self.course.id,
            'author': self.user.id
        }

        print(response.json())
        self.assertEquals(
            response.json(),
            body
        )

    def test_update_lesson(self):
        """Тест редактирования урока"""

        data = {
            'title': 'test_lesson_2',
            'description': 'test_description_2',
        }

        response = self.client.patch(
            reverse('lesson:update', args=[str(self.lesson.id)]),
            data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        body = {'id': self.lesson.id,
                'title': 'test_lesson_2',
                'imagine': None,
                'description': 'test_description_2',
                'video_link': 'https://www.youtube.com/watch?v=6EdAg5FdsGw',
                'course': self.course.id,
                'author': self.user.id
                }

        self.assertEquals(
            response.json(),
            body
        )

    def tet_delete_lesson(self):
        """Тест удаления урока"""

        response = self.client.delete(
            reverse('lesson:update', args=[str(self.lesson.id)])
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
