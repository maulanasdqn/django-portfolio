from django.urls import path
from . import viewsFrontend

urlpatterns = [
    path('', viewsFrontend.index, name='index'),
]