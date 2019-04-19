from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Doctor, RoomTypes, Room
from .forms import DoctorForm, RoomTypeForm, RoomForm


def index(request):
    return get_doctors(request)


def get_doctors(request):
    context = {
        'objects': Doctor.objects.all(),
    }
    return render(request, 'doctors/index.html', context)


def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return get_doctors(request)

    else:
        form = DoctorForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/doctor/add_doctor/',
        'title': 'doctor'
        })


def get_room_types(request):
    context = {
        'objects': RoomTypes.objects.all(),
    }
    return render(request, 'doctors/index.html', context)


def add_room_type(request):
    if request.method == 'POST':
        form = RoomTypeForm(request.POST)

        if form.is_valid():
            # RoomTypes(id=form.cleaned_data['room_type']).save()
            form.save()
            return get_room_types(request)

    else:
        form = RoomTypeForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/doctor/add_room_type/',
        'title': 'room type'
        })


def get_rooms(request):
    context = {
        'objects': Room.objects.all(),
    }
    return render(request, 'doctors/index.html', context)


def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)

        if form.is_valid():
            # RoomTypes(id=form.cleaned_data['room_type']).save()
            form.save()
            return get_rooms(request)

    else:
        form = RoomForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/doctor/add_room/',
        'title': 'room'
        })
