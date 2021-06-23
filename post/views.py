from django.shortcuts import render, HttpResponse

# Create your views here.


def contact(request):
    return HttpResponse('Office Address - 27, Alara street. <br> phone-09095000300 <br> email- hello@libertyng.com')

