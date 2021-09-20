from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import ImpDatesModel


# Create your views here.
class ImpDateCreate(CreateView):
    model = ImpDatesModel
    fields = ['name','occasion','date','remarks']


def home(request):
    pass
