from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from giftme.forms import TestForm


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
    pass
