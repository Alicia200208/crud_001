from django.test import TestCase
from django.urls import reverse
from .models import User


class BasicViewsTest(TestCase):
    def setUp(self):
        # create a dummy user for edit/view/delete
        self.user = User.objects.create(
            name='Test',
            email='test@example.com',
            password='secret',
            mobile_number='1234567890',
            date_of_birth='2000-01-01'
        )

    def test_user_list_page(self):
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listingpage.html')

    def test_add_page(self):
        response = self.client.get(reverse('add_user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add.html')

    def test_edit_page(self):
        response = self.client.get(reverse('edit_user', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit.html')

    def test_view_page(self):
        response = self.client.get(reverse('view_user', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view.html')

    def test_delete_page_get(self):
        response = self.client.get(reverse('delete_user', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete.html')

