from django.test import TestCase, Client
from django.urls import reverse
import json
#from home.models import (name of models)

class TestViews(TestCase):

  def setUp(self):
    self.client = Client()
    self.index_url = reverse('index')
    self.pricing_url = reverse('pricing')
    self.about_url = reverse('about')
    self.contactus_url = reverse('contactus')
    #if this needs args, self.track_url = reverse('track', args=['some-args']) or we could opt to use: self.project1 = Project.objects.create(name = 'project1', budget=10000)

  def test_index_GET(self):
    response = self.client.get(self.index_url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'home/index.html')
    #if we need to test out functions in views.py go to: https://www.youtube.com/watch?v=hA_VxnxCHbo&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=3 at 7:10

  def test_pricing_GET(self):
    response = self.client.get(self.pricing_url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'home/pricing.html')

  def test_about_GET(self):
    response = self.client.get(self.about_url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'home/about.html')

  def test_contactus_GET(self):
    response = self.client.get(self.contactus_url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'home/contactus.html')
