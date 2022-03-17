from django.contrib import admin

from .models import Parcel, Receiver, Sender

admin.site.register(Parcel)
admin.site.register(Receiver)
admin.site.register(Sender)
