from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from giftme.views import RegisterAPIView

urlpatterns = [
        path('register', RegisterAPIView.as_view()),
]
