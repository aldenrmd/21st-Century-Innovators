from django.db import models


class Parcel(models.Model):
    track_code = models.CharField(primary_key=True, max_length=100)
    pub_date = models.DateTimeField('date published')
    status = models.IntegerField(default=0)

    def __str__(self) -> str:
        return 'code: %s, status: %d' % (self.track_code, self.status)

class Province(models.Model):
    province_id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    province_id = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name