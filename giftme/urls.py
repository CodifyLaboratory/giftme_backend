from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

from giftme.views_ext.accounts import RegisterView, LogoutView, ProfileView
from giftme.views import IndexView, MyWishView, AddWishView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('accounts/profile/', ProfileView.as_view()),
    path('accounts/logout/', LogoutView.as_view(), name="logout"),
    path('accounts/register/', RegisterView.as_view(), name="register"),
    path('accounts/wishes/', MyWishView.as_view(), name='my_wishes'),
    path('wishes/add/', AddWishView.as_view(), name='add_my_wish'),
]