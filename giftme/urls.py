from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter

from giftme.views import RegisterAPIView, LoginAPIView, HolidayAPIView, LogoutAPIView, WishAPIView

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('holiday/', csrf_exempt(HolidayAPIView.as_view())),
]

router = DefaultRouter()
router.register(r'wish', WishAPIView, basename='wish')
urlpatterns += router.urls