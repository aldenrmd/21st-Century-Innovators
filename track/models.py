from django.db import models

# Create your models here.
class Tracker(models.Model):
  trackingcode = models.CharField(max_length=100)
  status = models.CharField(max_length=100)

  def __str__(self) -> str:
        return '%s %s' % (self.trackingcode, self.status)