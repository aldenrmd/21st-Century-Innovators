from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('track',views.track,name = 'track'),
    path('pricing',views.pricing,name = 'pricing'),
    path('about',views.about,name = 'about'),
    path('contactus',views.contactus,name = 'contactus'),
    path('admin', views.admin, name = 'admin'),
]