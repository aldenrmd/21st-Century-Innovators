from django.db import models

class admin_creds(models.Model):
  username = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  fullname = models.CharField(max_length=100)
  position = models.CharField(max_length=100)
  email = models.EmailField(max_length=200)

  def __str__(self) -> str:
    return 'Full name: %s, Position: %s, Email: %s' % self.fullname, self.position, self.email
