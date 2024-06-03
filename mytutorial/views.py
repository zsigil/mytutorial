#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
 #   return HttpResponse("Hello World. I am Django")
    return render(request, 'home.html')


def about(request):
#  return HttpResponse("This is about something.")
    return render(request, 'about.html')

