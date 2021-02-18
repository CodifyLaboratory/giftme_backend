from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from giftme.models import GiftMeUser, Test, Wish


class TestForm(ModelForm):
    class Meta:
        model = Test
        exclude = []


class RegisterForm(UserCreationForm):
    class Meta:
        model = GiftMeUser
        fields = ["email"]
        #exclude=[]


class UserForm(ModelForm):
    class Meta:
        model = GiftMeUser
        exclude = []


class AddWishForm(ModelForm):
    class Meta:
        model = Wish
        exclude = []