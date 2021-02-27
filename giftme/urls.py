from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from giftme.views import RegisterAPIView, LoginAPIView

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login')
]
