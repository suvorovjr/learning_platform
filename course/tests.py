from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from users.models import User
from course.models import Course


class CourseTestCase(APITestCase):
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

    def test_course_create(self):
        """"""
        data = {
            'title': 'test_course_2',
            'description': 'test_description_2',
            'author': self.user.id
        }

        response = self.client.post(
            '/course/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        body = {
            'id': self.course.id + 1,
            'lesson_count': 0,
            'title': 'test_course_2',
            'imagine': None,
            'description': 'test_description_2',
            'author': self.user.id
        }

        self.assertEquals(
            response.json(),
            body
        )

    def test_list_course(self):
        """"""

        response = self.client.get(
            '/course/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        body = [
            {
                'id': self.course.id,
                'lesson_count': 0,
                'title': 'test_course',
                'imagine': None,
                'description': 'test_description',
                'author': self.user.id
            }
        ]

        self.assertEquals(
            response.json()['results'],
            body
        )

    def test_retrieve_course(self):
        """"""

        response = self.client.get(
            f'/course/{self.course.id}/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        body = {
            'id': self.course.id,
            'lesson_count': 0,
            'title': 'test_course',
            'imagine': None,
            'description': 'test_description',
            'author': self.user.id
        }

        self.assertEquals(
            response.json(),
            body
        )

    def test_update_course(self):
        """"""

        data = {
            'title': 'test_course_1',
            'description': 'test_description_1'
        }
        response = self.client.patch(
            f'/course/{self.course.id}/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        body = {
            'id': self.course.id,
            'lesson_count': 0,
            'title': 'test_course_1',
            'imagine': None,
            'description': 'test_description_1',
            'author': self.user.id
        }

        self.assertEquals(
            response.json(),
            body
        )

    def test_destroy_course(self):
        """"""

        response = self.client.delete(
            f'/course/{self.course.id}/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
