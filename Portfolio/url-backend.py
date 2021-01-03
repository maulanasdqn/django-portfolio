from django.urls import path
from . import viewsBackend

urlpatterns = [
    path('dashboard/', viewsBackend.panel, name='dashboard'),
    path('content/', viewsBackend.content, name='content'),
    path('user/', viewsBackend.user, name='user'),
    path('profile/', viewsBackend.profile, name='profile')
]