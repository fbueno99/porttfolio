from django.shortcuts import render


def port(request):
    return render(request, "mysite/port.html")

def index(request):
    return render(request, "mysite/index.html")

# Create your views here.
