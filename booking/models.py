from django.db import models

# Create your models here.
class Sender(models.Model):
    sender_first_name = models.CharField(max_length=50)
    sender_last_name = models.CharField(max_length=50)
    sender_number = models.CharField(max_length=15)
    sender_email = models.EmailField(max_length=100)
    sender_address = models.CharField(max_length=100)
    sender_state = models.CharField(max_length=100)
    sender_zip = models.CharField(max_length=15)
    sender_city = models.CharField(max_length=100)
    sender_country = models.CharField(max_length=100)
    trackingcode = models.CharField(max_length=100)
    def __str__(self) -> str:
        return '%s %s' % (self.sender_first_name, self.sender_last_name)


class Receiver(models.Model):
    receiver_first_name = models.CharField(max_length=50)
    receiver_last_name = models.CharField(max_length=50)
    receiver_number = models.CharField(max_length=15)
    receiver_email = models.EmailField(max_length=100)
    receiver_address = models.CharField(max_length=100)
    receiver_state = models.CharField(max_length=100)
    receiver_zip = models.CharField(max_length=15)
    receiver_city = models.CharField(max_length=100)
    receiver_country = models.CharField(max_length=100)
    trackingcode = models.CharField(max_length=100)
    def __str__(self) -> str:
        return '%s %s' % (self.receiver_first_name, self.receiver_last_name)

