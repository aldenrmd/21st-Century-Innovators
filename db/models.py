from django.db import models


class Parcel(models.Model):
    track_code = models.CharField(primary_key=True, max_length=100)
    pub_date = models.DateTimeField('date published')
    status = models.IntegerField(default=0)

    def __str__(self) -> str:
        return 'code: %s, status: %d' % self.track_code, self.status


class Receiver(models.Model):
    parcel = models.OneToOneField(Parcel, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_num = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    street_num = models.CharField(max_length=100)
    province_id = models.CharField(max_length=100)
    city_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return 'name %s %s, code: %s' % self.first_name, self.last_name, self.parcel.track_code


class Sender(models.Model):
    parcel = models.OneToOneField(Parcel, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_num = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    street_num = models.CharField(max_length=100)
    province_id= models.CharField(max_length=100)
    city_id= models.CharField(max_length=100)

    def __str__(self) -> str:
        return 'name %s %s, code: %s' % self.first_name, self.last_name, self.parcel.track_code


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