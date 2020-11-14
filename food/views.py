from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Item


def index (request):
    item_list = Item.objects.all()
    tempalte = loader.get_template("food.html")
    context ={

    }
    return HttpResponse(tempalte.render(context , request))
    
    # return HttpResponse("hello world") # example of HttpResponse

def item (request):
    return HttpResponse("<h1> this is item site </h1>")