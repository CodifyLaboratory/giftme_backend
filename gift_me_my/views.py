from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from gift_me_my.forms import TestForm, HolidayForm
from gift_me_my.models import Test, Holiday


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


class MyProfileView(TemplateView):
    template_name = 'profile/my_profile.html'

    def dispatch(self, request, *args, **kwargs):
        holidays = Holiday.objects.all()
        return render(request, self.template_name , context={
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
