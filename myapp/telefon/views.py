from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse

from .models import Phones


# def index(request):
#     return HttpResponse("PHONE")

def index(request):
    pph = Phones.objects.order_by('-published')
    return render(request, 'myapp/index.html', {'pph': pph})