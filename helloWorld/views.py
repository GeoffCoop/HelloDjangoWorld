#from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    returnString = "Hello, World!    " + datetime.datetime.now().strftime("%H:%M:%S   %B %d, %Y")
    return HttpResponse(returnString)
