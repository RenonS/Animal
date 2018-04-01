from django.shortcuts import render, redirect
from animal.models import Advert
from django.contrib import auth
from django.contrib.auth import get_user
from django.http.response import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def index(request):
    data = {"adverts": Advert.objects.all(), "list": Advert.category_list}
    return render(request, "index.html", context=data)


def advert(request, advert_id=1):
    data = {"advert": Advert.objects.get(id=advert_id)}
    return render(request, "advert.html", context=data)


def auth(request):
    return render(request, "auth.html")
