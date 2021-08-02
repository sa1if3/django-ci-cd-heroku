from django.test import TestCase
from django.urls import reverse
from names.models import SampleName


class SampleNameListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        SampleName.objects.create(first_name='Big', last_name='Bob')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/show/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('show'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('show'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'show.html')
