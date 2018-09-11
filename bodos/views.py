from django.shortcuts import render


def index(request):
    return render( request, 'bodos/index.html')

def login(request):
    return render( request, 'bodos/login.html')

def register(request):
    return render( request, 'bodos/register.html')