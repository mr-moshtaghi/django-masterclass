from django.shortcuts import render
from django.http import HttpResponse

from .models import Item


def index (request):
    item_list = Item.objects.all()
    context = {
        'item_list' : item_list,
    }
    return render(request , "food.html" , context)


    # example of HttpResponse
    #return HttpResponse(tempalte.render(context , request)) 
    # return HttpResponse("hello world") 

def item (request):
    return HttpResponse("<h1> this is item site </h1>")


def detail(request , item_id):    # item_id ---------> <int:item_id> in path("<int:item_id>/" , views.detail , name="detail")
    item = Item.objects.get(pk = item_id)
    context = {
        "item" : item,
    }
    return render(request , "detail.html" , context) 