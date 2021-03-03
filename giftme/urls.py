from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from giftme.views import RegisterAPIView, LoginAPIView, HolidayAPIView

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('holiday/', csrf_exempt(HolidayAPIView.as_view())),
]
