from django.http import HttpResponse
import random
from django.shortcuts import render

# Create your views here.

# function based view


def home(request):

    num = random.randint(0, 10000000)
    return render(
        request, 'base.html',
        {'data_from_py': 'This is coming from py file', 'num': num}
    )
