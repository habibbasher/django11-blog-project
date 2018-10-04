from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
import random
from django.shortcuts import render

# Create your views here.


def about(request):
    context = {}
    return render(request, 'about.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        num = random.randint(0, 10000000)
        context = {
            'data_from_py': True,
            'num': num,
            'some_list': [
                num,
                random.randint(0, 10000000),
                random.randint(0, 10000000)
            ]
        }
        return context


# class AboutView(TemplateView):
#     template_name = 'about.html'
#
#
# class ContactView(TemplateView):
#     template_name = 'contact.html'
