from django.urls import path
from . import viewsBackend

urlpatterns = [
    path('dashboard/', viewsBackend.panel, name='dashboard'),
    path('content/', viewsBackend.content, name='content')
]