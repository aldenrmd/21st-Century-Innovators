from django.test import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):
  def setUp(self):
    self.client = Client()
    self.results_url = reverse('results')
    self.track_url = reverse('track')

  def test_track_GET(self):
    response = self.client.get(self.track_url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'track/track.html')

  def test_results_GET(self):
    response = self.client.get(self.results_url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'track/results.html')