from django.test import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):
  
  def setUp(self):
    self.client = Client()
    self.booking_url = reverse('booking')
    self.update_url = reverse('update')
    self.search_url = reverse('search')

  def test_booking_GET(self):
    response = self.client.get(self.booking_url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'booking/booking.html')

  def test_update_GET(self):
    response = self.client.get(self.update_url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'booking/update.html')

  def test_search_GET(self):
    response = self.client.get(self.search_url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'booking/search.html')

# POST Requests to be updated.