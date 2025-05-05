from django.contrib.auth import get_user_model

from django.test import TestCase

from django.urls import reverse

from .models import Emp


# Create your tests here.

class BlogTests(TestCase):


    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'secret'
        )

        self.emp=Emp.objects.create(
            name = 'Andrey',
            emp_id = '3222',
            phone = '454634',
            address = 'Vologda',
            working = True,
            department = 'Management'
        )
    def test_string_representation(self):

        emp = Emp(name = 'just a name')
        self.assertEqual(str(emp), emp.name)

    def test_emp_content(self):

        self.assertEqual(f'{self.emp.name}', 'Andrey')
        self.assertEqual(f'{self.emp.emp_id}', '3222')
        self.assertEqual(f'{self.emp.phone}', '454634')
        self.assertEqual(f'{self.emp.address}', 'Vologda')
        self.assertEqual(f'{self.emp.working}', 'True')
        self.assertEqual(f'{self.emp.department}', 'Management')


    def test_emp_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Andrey')
        self.assertTemplateUsed(response, 'home.html')


    def test_emp_detail_view(self):
        response = self.client.get('/emp/1/')
        no_response = self.client.get('/emp/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Andrey')
        self.assertTemplateUsed(response, 'emp_detail.html')


















