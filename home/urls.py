from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('pricing',views.pricing,name = 'pricing'),
    path('about',views.about,name = 'about'),
    path('contactus',views.contactus,name = 'contactus'),
]