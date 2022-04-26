from django.test import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):
  
  def setUp(self):
    self.client = Client()
    self.booking_url = reverse('booking')

  def test_booking_GET(self):
    response = self.client.get(self.booking_url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'booking/booking.html')
