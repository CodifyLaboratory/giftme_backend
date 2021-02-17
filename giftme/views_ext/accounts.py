from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from giftme.forms import RegisterForm


class ProfileView(View):
    def dispatch(self, request, *args, **kwargs):
        return redirect(reverse("index"))


class LogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect("index")


class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse("index"))
        form = RegisterForm()

        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Вы успешно зарегистрировались, теперь войдите в ситему")
                return redirect(reverse("login"))
        return render(request, self.template_name, {
            "form": form
        })