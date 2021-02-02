from django.contrib.admin import site

from gift_me_my.models import Test, CustomUser

site.register(Test)
site.register(CustomUser)