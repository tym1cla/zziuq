from django.urls import path
from .views import*

urlpatterns = [
    path('', login_user),
    path('index/', index),
    path('register/', register),
    path('info/', info),
]