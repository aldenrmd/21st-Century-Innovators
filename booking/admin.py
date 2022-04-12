from django.contrib import admin
from .models import Receiver, Sender

# Register your models here.
admin.site.register(Receiver)
admin.site.register(Sender)