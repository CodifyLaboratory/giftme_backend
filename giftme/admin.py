from django.contrib import admin

from giftme.models import GiftMeUser, Wish, Holiday, Profile

admin.site.register(GiftMeUser)
admin.site.register(Wish)
admin.site.register(Holiday)
admin.site.register(Profile)
