from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()

        # we needd to get our user model get all objects
        # of this model and call create_superuser fucntion

        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@londonappdev.com',
            password='password123'
        )

        # login our superuser
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            email='me@smirnovsergs.com',
            password='password123',
            name='Test User Full Name',  # ( sic!)
        )

    def test_user_listed(self):
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_page_change(self):
        url = reverse('admin:core_user_change', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(res.status_code, 200)
