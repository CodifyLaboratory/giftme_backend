from django.contrib import admin

from giftme.models import GiftMeUser, Wish, Holiday

admin.site.register(GiftMeUser)
admin.site.register(Wish)
admin.site.register(Holiday)
