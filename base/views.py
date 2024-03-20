from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("This is Home Page.")


def detail(request, person_id):
    return HttpResponse(f"You are looking at person {person_id}.")


def items(request, item_id):
    return HttpResponse(f"You are looking at items of owner" % item_id)


