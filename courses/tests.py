from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *

class CoursesTests(APITestCase):
    def setUp(self):
        user = User.objects.create_superuser(username='tester',password="pass",email="test@example.com")
        self.client.force_authenticate(user=user)
        # the category needs to be first created
        Category.objects.create(name="Python",imgpath="img.jpg")
        self.data = {
            "name": "Python",
            "description": "best language",
            "category": 1,
            "logo": "logo.jpg",
            "branches": [
                {
                    "latitude": "1.1",
                    "longitude": "2.2",
                    "address": "Manas 101"
                }
            ],
            "contacts": [
                {
                    "type": 3,
                    "value": "aisuluu@example.com"
                }
            ]
        }

    def test_create_course(self):
        """
        Ensure we can create a new course object.
        """
        url = reverse('create')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 1)
        self.assertEqual(Course.objects.get().name, 'Python')
        # test all course properties is correct
        self.assertEqual(Course.objects.get().branches.all()[0].address, 'Manas 101')
        # test all branch properties are correct
        # test all contact properties are correct

    def test_get_course_list(self):
        # reverse takes the "name" used in the urls.py for the courses route
        # create is not the correct name, since it can be used for more than creating
        # but can also be used for getting a list
        url = reverse('create')
        create_response1 = self.client.post(url, self.data, format='json')
        create_response2 = self.client.post(url, self.data, format='json')
        get_response = self.client.get(url, format='json')
        self.assertEqual(create_response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(create_response2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_response.data, [self.data, self.data])

    def test_get_course_detail(self):
        self.fail("please implement this test")

    def test_update_course_detail(self):
        self.fail("please implement this test")

    def test_delete_course_detail(self):
        self.fail("please implement this test")

#class CategoryTests(APITestCase):
    # why are categories not auto created like branches and contacts?
    # I don't remember your specs, you should make sure it's correct.
    # if we do need to create categories separate from Courses, we should
    # also test them here.
