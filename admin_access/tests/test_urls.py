from django.test import SimpleTestCase
from django.urls import reverse, resolve
from admin_access.views import dashboard, login

class TestUrls(SimpleTestCase):

  def test_dashboard_url_resolves(self):
    url = reverse('dashboard')
    print(resolve(url))
    self.assertEquals(resolve(url).func, dashboard)

def test_login_url_resolves(self):
    url = reverse('login')
    print(resolve(url))
    self.assertEquals(resolve(url).func, login)