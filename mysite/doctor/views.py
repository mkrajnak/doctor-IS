from django.shortcuts import render
from .models import *
from .forms import *


def index(request):
    return render(request, 'index.html', None)


def get_departments(request):
    return render(request, 'doctors/index.html', {
        'objects': Department.objects.all(),
    })


def get_room_types(request):
    return render(request, 'doctors/index.html', {
        'objects': RoomTypes.objects.all(),
    })


def get_rooms(request):
    return render(request, 'doctors/index.html', {
        'objects': Room.objects.all(),
    })


def get_doctors(request):
    return render(request, 'doctors/index.html', {
        'objects': Doctor.objects.all(),
    })


def get_nurses(request):
    return render(request, 'doctors/index.html', {
        'objects': Nurse.objects.all(),
    })


def get_patients(request):
    return render(request, 'doctors/index.html', {
        'objects': Patient.objects.all(),
    })


def get_drugs(request):
    return render(request, 'doctors/index.html', {
        'objects': Drugs.objects.all(),
    })


def get_treatments(request):
    return render(request, 'doctors/index.html', {
        'objects': Treatments.objects.all(),
    })


def get_diseases(request):
    return render(request, 'doctors/index.html', {
        'objects': Diseases.objects.all(),
    })


def get_visits(request):
    return render(request, 'doctors/index.html', {
        'objects': Visit.objects.all(),
    })


def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return get_doctors(request)
    else:
        form = DepartmentForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/doctor/add_department/',
        'title': 'Department'
        })


def add_room_type(request):
    if request.method == 'POST':
        form = RoomTypeForm(request.POST)

        if form.is_valid():
            form.save()
            return get_room_types(request)

    else:
        form = RoomTypeForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/doctor/add_room_type/',
        'title': 'Room type'
        })


def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return get_rooms(request)
    else:
        form = RoomForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/doctor/add_room/',
        'title': 'Room'
        })


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
        'title': 'Doctor'
        })


def add_nurse(request):
    if request.method == 'POST':
        form = NurseForm(request.POST)
        if form.is_valid():
            form.save()
            return get_nurses(request)
    else:
        form = NurseForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/doctor/add_nurse/',
        'title': 'Nurse'
        })


def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return get_patients(request)
    else:
        form = PatientForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/doctor/add_patient/',
        'title': 'Patient'
        })


def add_drugs(request):
    if request.method == 'POST':
        form = DrugsForm(request.POST)
        if form.is_valid():
            form.save()
            return get_drugs(request)
    else:
        form = DrugsForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/doctor/add_drugs/',
        'title': 'Drug'
        })


def add_treatments(request):
    if request.method == 'POST':
        form = TreatmentsForm(request.POST)
        if form.is_valid():
            form.save()
            return get_treatments(request)
    else:
        form = TreatmentsForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/doctor/add_treatments/',
        'title': 'Treatment'
        })


def add_diseases(request):
    if request.method == 'POST':
        form = DiseasesForm(request.POST)
        if form.is_valid():
            form.save()
            return get_diseases(request)
    else:
        form = DiseasesForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/doctor/add_diseases/',
        'title': 'Disease'
        })


def add_visits(request):
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return get_visits(request)
    else:
        form = VisitForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/doctor/add_visits/',
        'title': 'Visit'
        })
