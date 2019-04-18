from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Doctor


def index(request):
    return HttpResponse("Hello, world.")


def get_doctors(request):
    # response = ["Your doctor is %s." %x.first_name for x in Doctor.objects.all()]
    context = {
        'doctors': Doctor.objects.all(),
    }
    return render(request, 'doctors/index.html', context)


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'doctors/index.html', context)
    return False
