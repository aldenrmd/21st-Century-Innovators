from django.db import models


class credential(models.Model):
  username = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  fullname = models.CharField(max_length=100)
  position = models.CharField(max_length=100)
  email = models.CharField(max_length=100)

  def __str__(self) -> str:
    return 'Full name: %s, Position: %s, Email: %s' % (self.fullname, self.position, self.email)