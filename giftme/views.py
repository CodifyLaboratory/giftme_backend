from http.client import HTTPResponse

from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from giftme.forms import TestForm, AddWishForm, HolidayForm
from giftme.models import Wish, Holiday


class IndexView(TemplateView):
    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):
        form = TestForm()
        if request.method == "POST":
            form = TestForm(request.POST)
            if form.is_valid():
                form.instance.name = request.user
                form.save()
                return redirect("index")
        return render(request, self.template_name, {"form": form})


class MyWishView(TemplateView):
    template_name = 'mywish.html'

    def dispatch(self, request, *args, **kwargs):
        wishes = Wish.objects.all()

        return render(request, self.template_name, context={
            "wishes": wishes
        })


class AddWishView(TemplateView):
    template_name = 'add_wish.html'

    def dispatch(self, request, *args, **kwargs):
        form = AddWishForm

        if request.method == "POST":
            form = AddWishForm(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, "Желание успешно добавлено в список")
                return redirect('/')
        return render(request, self.template_name, {"form": form})


class MyProfileView(TemplateView):
    template_name = 'profile/my_profile.html'

    def dispatch(self, request, *args, **kwargs):
        holidays = Holiday.objects.all()
        return render(request, self.template_name, context={
            "holidays": holidays
        })


class AddHolidayView(TemplateView):
    template_name = "profile/add_holiday.html"

    def dispatch(self, request, *args, **kwargs):
        form = HolidayForm()
        if request.method == "POST":
            form = HolidayForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/")
        return render(request, self.template_name, {"form": form})
