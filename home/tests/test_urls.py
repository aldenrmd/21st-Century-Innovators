from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index, pricing, about, contactus

class TestUrls(SimpleTestCase):

  def test_index_url_resolves(self):
    url = reverse('index')
    print(resolve(url))
    self.assertEquals(resolve(url).func, index)

  def test_pricing_url_resolves(self):
    url = reverse('pricing')
    print(resolve(url))
    self.assertEquals(resolve(url).func, pricing)

  def test_about_url_resolves(self): 
    url = reverse('about') #if it needs args, url = reverse('about', args=['some-args'])
    print(resolve(url))
    self.assertEquals(resolve(url).func, about)

  def test_contactus_url_resolves(self):
    url = reverse('contactus')
    print(resolve(url))
    self.assertEquals(resolve(url).func, contactus) #if class file, self.assertEquals(resolve(url).func.view_class, contactus)