from django.test import TestCase
from db.models import Parcel, Province, City

class TestModels(TestCase):
  
  def setUp(self):
    Parcel.objects.create(track_code="Kobe Bryant", status=0)
    Province.objects.create(province_id=(True,"9200"), name="Cebu Province")
    City.objects.create(city_id=(True, "5000"), name="randomCity")