from django.contrib.auth import get_user_model

from django.test import Client, TestCase

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


    def test_get_absolute_url(self):

        self.assertEquals(self.emp.get_absolute_url(), '/emp/1/')


    def test_emp_create_view(self):

        response = self.client.post(reverse('emp_new'), { 'name':'New'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New')
        #self.assertContains(response, '12')
        #self.assertContains(response, '25')
        #self.assertContains(response, 'NewA')
        #self.assertContains(response, 'True')
        #self.assertContains(response, 'NewD')


    def test_emp_update_view(self):

        response = self.client.post(reverse('emp_edit', args='1'), { 
                                   'name': 'Updated name',
                                   'emp_id': 'Updated emp_id',
                                   'phone': '1phone',
                                   'address': 'Updated address',
                                   'working': 'False',
                                   'department': 'Updated department'

        })
        self.assertEqual(response.status_code, 302)


    def test_emp_delete_view(self):

        response = self.client.get(reverse('emp_delete', args='1')) 
        
        self.assertEqual(response.status_code, 200)







        























