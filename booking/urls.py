from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.booking, name = 'booking'),
    path('search/', views.search, name='search'),
    path('update/',views.update, name='update')
]