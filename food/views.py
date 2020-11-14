from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    return HttpResponse("hello world")

def item (request):
    return HttpResponse("<h1> this is item site </h1>")