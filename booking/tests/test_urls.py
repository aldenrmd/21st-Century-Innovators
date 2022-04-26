from django.test import TestCase
from django.test import SimpleTestCase
from booking.views import booking
from django.urls import reverse, resolve

class TestUrls(SimpleTestCase):

  def test_booking_url_resolves(self):
    url = reverse('booking')
    print(resolve(url))
    self.assertEquals(resolve(url).func, booking)