from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from gift_me_my.models import Test, GiftMeUser


class TestForm(ModelForm):
    class Meta:
        model = Test
        exclude = []

class RegisterForm(UserCreationForm):
    class Meta:
        model = GiftMeUser
        fields=["email"]
        #exclude=[]

class UserForm(ModelForm):
    class Meta:
        model = GiftMeUser
        exclude = []
