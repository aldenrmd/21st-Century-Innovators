from django.test import SimpleTestCase
from django.urls import reverse, resolve
from track.views import results, track

class TestUrls(SimpleTestCase):

  def test_track_url_resolves(self):
    url = reverse('track')
    print(resolve(url))
    self.assertEquals(resolve(url).func, track)

  def test_results_url_resolves(self):
    url = reverse('results')
    print(resolve(url))
    self.assertEquals(resolve(url).func, results)