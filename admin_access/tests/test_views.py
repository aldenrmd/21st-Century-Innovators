from django.test import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):

  def setUp(self):
    self.client = Client()
    self.login_url = reverse('login')
    self.dashboard_url = reverse('dashboard') 

  def test_dashboard_GET(self):
    response = self.client.get(self.dashboard_url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'admin_access/dashboard.html')

  def test_login_GET(self):
    response = self.client.get(self.login_url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'admin_access/admin.html')
# Create your tests here.
