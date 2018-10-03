from django.http import HttpResponse
import random
from django.shortcuts import render

# Create your views here.

# function based view


def home(request):

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
    return render(request, 'home.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)
