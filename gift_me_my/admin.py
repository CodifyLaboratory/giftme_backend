from django.contrib.admin import site

from gift_me_my.models import Test, GiftMeUser

site.register(Test)
site.register(GiftMeUser)