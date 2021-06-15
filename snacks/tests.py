from django.test import TestCase
from django.views.generic.edit import CreateView 
from django.urls import reverse
from django.test import SimpleTestCase 


class snack_test(SimpleTestCase):
    def test_snacks(self):
        # arrange
        # assign
        url=reverse("list_view")
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
# assert

# Create your tests here.

