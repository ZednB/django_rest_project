from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson, Course, CourseSubscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        """Создание тестового пользователя"""
        self.user = User.objects.create(email='test@mail.ru', password='12345')
        self.course = Course.objects.create(name='testcourse', owner=self.user)
        self.lesson = Lesson.objects.create(name='testlesson', course=self.course, owner=self.user)
        self.lesson2 = Lesson.objects.create(name='testlesson2', course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        """Тест на создание урока"""
        data = {
            'name': self.lesson.name,
            'course': self.course.id,
            'video_url': 'https://www.youtube.com/'
        }
        response = self.client.post('/lesson/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 3)

    def test_get_lessons(self):
        response = self.client.get('/lesson/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_lesson(self):
        data = {
            'name': 'test',
            'course': self.course.pk,
            'owner': self.user.pk,
            'video_url': 'https://www.youtube.com/'
        }
        response = self.client.put(f'/lesson/update/{self.lesson.pk}/', data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_retrieve_lesson(self):
        data = {
            'name': 'test',
            'course': self.course.pk,
            'owner': self.user.pk,
            'video_url': 'https://www.youtube.com/'
        }
        response = self.client.get(f'/lesson/{self.lesson.pk}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_lesson(self):
        response = self.client.delete(f'/lesson/destroy/{self.lesson.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CourseSubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@mail.ru', password='12345')
        self.course = Course.objects.create(name='testcourse', owner=self.user)

    def test_subscribe_to_course(self):
        url = '/subscription/'
        data = {'course_id': self.course.id}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
