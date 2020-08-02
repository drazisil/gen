from django.test import Client, TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory

# Create your tests here.
client = Client()


class PonyLookupTests(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_that_pony_id_positive(self):
        """
        views:fetch_pony() fails when passed a non-positive number
        """
        response = self.client.post(reverse('api:pony_lookup'), data={'pony': -2})

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.content, b'The pony id must be a number greater then 0.')

    def test_that_pony_id_positive_2(self):
        """
        views:fetch_pony() fails when passed a non-positive number
        """
        response = self.client.post(reverse('api:pony_lookup'), data={'pony': -2})

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.content, b'The pony id must be a number greater then 0.')
