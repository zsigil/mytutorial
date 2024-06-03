from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello World. I am Django")


def about(request):
    return HttpResponse("This is about something.")

