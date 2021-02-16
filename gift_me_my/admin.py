from django.contrib.admin import site

from gift_me_my.models import Test, GiftMeUser, Holiday

site.register(Test)
site.register(GiftMeUser)
site.register(Holiday)
