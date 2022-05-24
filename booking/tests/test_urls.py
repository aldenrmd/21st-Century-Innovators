from django.test import SimpleTestCase
from booking.views import booking, update, search
from django.urls import reverse, resolve

class TestUrls(SimpleTestCase):

  def test_booking_url_resolves(self):
    url = reverse('booking')
    print(resolve(url))
    self.assertEquals(resolve(url).func, booking)

  def test_update_url_resolves(self):
    url = reverse('update')
    print(resolve(url))
    self.assertEquals(resolve(url).func, update)

  def test_search_url_resolves(self):
    url = reverse('search')
    print(resolve(url))
    self.assertEquals(resolve(url).func, search)