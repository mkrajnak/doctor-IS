from django.shortcuts import render
from .models import Doctor


def index(request):
    return HttpResponse("Hello, world.")


def get_doctors(request):
    # response = ["Your doctor is %s." %x.first_name for x in Doctor.objects.all()]
    context = {
        'doctors': Doctor.objects.all(),
    }
    return render(request, 'doctors/index.html', context)
