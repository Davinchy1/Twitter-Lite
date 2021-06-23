from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Hi all, I choose to be dedicated <br> to my study of Django <br> This is my pledge! </h1>')