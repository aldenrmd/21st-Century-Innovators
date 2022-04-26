from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.track, name = 'track'),
    path('results/', views.results, name = 'results'),
]